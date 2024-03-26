# Demo Google Drive Connector

This is a demo Google Drive connector used in LLM University's Chat with Retrieval-Augmented Generation module. Read the [article](https://txt.cohere.com/rag-chatbot-connector/) to learn more.

## Limitations

Currently this connector can only search for Google Docs, Google Sheets, and Google Slide files. It does not support searching for other file types.

## Authentication

This connector supports two types of authentication: Service Account and OAuth.

### Service Account

For service account authentication this connector requires two environment variables:

#### `GDRIVE_SERVICE_ACCOUNT_INFO`

The `GDRIVE_SERVICE_ACCOUNT_INFO` variable should contain the JSON content of the service account credentials file. To get the credentials file, follow these steps:

1. [Create a project in Google Cloud Console](https://cloud.google.com/resource-manager/docs/creating-managing-projects).
2. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts) and [activate the Google Drive API](https://console.cloud.google.com/apis/api/drive.googleapis.com) in the Google Cloud Console.
3. [Create a service account key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) and download the credentials file as JSON. The credentials file should look like this:

```json
{
  "type": "service_account",
  "project_id": "{project id}",
  "private_key_id": "{private_key_id}",
  "private_key": "{private_key}",
  "client_email": "{client_email}",
  "client_id": "{client_id}",
  "auth_uri": "{auth_uri}",
  "token_uri": "{token_uri}",
  "auth_provider_x509_cert_url": "{auth_provider_x509_cert_url}",
  "client_x509_cert_url": "{client_x509_cert_url}",
  "universe_domain": "{universe_domain}"
}
```

4. Convert the JSON credentails to a string through `json.dumps(credentials)` and save the result in the `GDRIVE_SERVICE_ACCOUNT_INFO` environment variable.
5. Make sure to [share the folder(s) you want to search with the service account email address](https://support.google.com/a/answer/7337554?hl=en).

#### `GDRIVE_CONNECTOR_API_KEY`

The `GDRIVE_CONNECTOR_API_KEY` should contain an API key for the connector. This value must be present in the `Authorization` header for all requests to the connector.

### OAuth

When using OAuth for authentication, the connector does not require any additional environment variables. Instead, the OAuth flow should occur outside of the Connector and Cohere's API will forward the user's access token to this connector through the `Authorization` header.

With OAuth the connector will be able to search any Google Drive folders that the user has access to.

## Optional Configuration

This connector also supports a few optional environment variables to configure the search:

1. `GDRIVE_SEARCH_LIMIT` - Number of results to return. Default is 10.
2. `GDRIVE_FOLDER_ID` - ID of the folder to search in. If not provided, the search will be performed in the whole drive.

## Development

Create a virtual environment and install dependencies with poetry. We recommend using in-project virtual environments:

```bash
  $ poetry config virtualenvs.in-project true
  $ poetry install --no-root
```

Next, start up the search connector server:

```bash
  $ poetry shell
  $ flask --app provider --debug run --port 5000
```

and check with curl to see that everything works:

```bash
  $ curl --request POST \
    --url http://localhost:5000/search \
    --header 'Content-Type: application/json' \
    --data '{
    "query": "stainless propane griddle"
  }'
```

Alternatively, load up the Swagger UI and try out the API from a browser: http://localhost:5000/ui/
