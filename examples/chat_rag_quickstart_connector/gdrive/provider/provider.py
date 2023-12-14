import logging
from flask import current_app as app
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from . import UpstreamProviderError, async_download

CSV_MIMETYPE = "text/csv"
TEXT_MIMETYPE = "text/plain"
SCOPES = [
    "https://www.googleapis.com/auth/drive.metadata.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]
SEARCH_MIME_TYPES = [
    "application/vnd.google-apps.document",
    "application/vnd.google-apps.spreadsheet",
    "application/vnd.google-apps.presentation",
]
DOC_FIELDS = (
    "id, name, mimeType, webViewLink, lastModifyingUser, modifiedTime, exportLinks"
)

logger = logging.getLogger(__name__)


def process_data_with_service(data, request_credentials: Credentials):
    results = []
    files = data.get("files", [])
    if not files:
        logger.debug("No files found.")
        return results

    id_to_urls = extract_links(files)
    id_to_texts = async_download.perform(id_to_urls, request_credentials.token)

    for _file in files:
        id = _file.get("id")
        if id is None:
            continue

        text = id_to_texts.get(id)
        if text is None:
            continue

        title = _file.pop("name", None)
        url = _file.pop("webViewLink", None)
        modifiedTime = _file.pop("modifiedTime", None)
        lastModifyingUser = _file.pop("lastModifyingUser", None)

        data_to_append = _file
        data_to_append["text"] = text
        if title:
            data_to_append["title"] = title
        if url:
            data_to_append["url"] = url
        if modifiedTime:
            data_to_append["modifiedTime"] = modifiedTime
        if lastModifyingUser and "displayName" in lastModifyingUser:
            data_to_append["editedBy"] = lastModifyingUser["displayName"]
        results.append(data_to_append)

    return results


def extract_links(files) -> [str, str]:
    id_to_urls = dict()
    for _file in files:
        export_links = _file.pop("exportLinks", {})
        id = _file.get("id")
        if id is None:
            continue

        if TEXT_MIMETYPE in export_links:
            id_to_urls[id] = export_links[TEXT_MIMETYPE]
        elif CSV_MIMETYPE in export_links:
            id_to_urls[id] = export_links[CSV_MIMETYPE]
    return id_to_urls


def split_and_remove_stopwords(text: str):
    # Tokenize the input text
    words = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    return filtered_words


def request_credentials(access_token=None):
    if service_account_info := app.config.get("SERVICE_ACCOUNT_INFO"):
        logger.debug("Using service account credentials")
        credentials = service_account.Credentials.from_service_account_info(
            service_account_info, scopes=SCOPES
        )
        if credentials.expired or not credentials.valid:
            credentials.refresh(Request())

        return credentials
    elif access_token:
        logger.debug("Using oauth credentials")
        return Credentials(access_token)
    else:
        raise AssertionError("No service account or oauth credentials provided")


def search(query, access_token=None):
    service = build("drive", "v3", credentials=request_credentials(access_token))

    # Google Drive's API search will attempt to match the search query exactly
    # which leads to poor results. We split the query into words and remove stop words
    # to improve the search results.
    query_words = split_and_remove_stopwords(query)

    conditions = [
        "("
        + " or ".join([f"mimeType = '{mime_type}'" for mime_type in SEARCH_MIME_TYPES])
        + ")",
        "("
        + " or ".join([f"fullText contains '{word}'" for word in query_words])
        + ")",
    ]

    if gdrive_folder_id := app.config.get("FOLDER_ID", None):
        conditions.append(f"'{gdrive_folder_id}' in parents ")

    q = " and ".join(conditions)
    page_size = app.config.get("SEARCH_LIMIT", 10)
    fields = f"nextPageToken, files({DOC_FIELDS})"
    try:
        search_results = (
            service.files()
            .list(
                pageSize=page_size,
                fields=fields,
                q=q,
            )
            .execute()
        )
    except HttpError as http_error:
        raise UpstreamProviderError(message=str(http_error)) from http_error

    return process_data_with_service(search_results, request_credentials(access_token))