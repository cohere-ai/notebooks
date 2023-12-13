import logging

from connexion.exceptions import Unauthorized
from flask import current_app as app
from provider.documents import Documents

logger = logging.getLogger(__name__)

demo_store = {}


# This function is run for the /search endpoint
# the results that are returned here will be passed to Cohere's model for RAG
def search(body):
    logger.debug(f'Search request: {body["query"]}')

    try:
        docs = demo_store["docs"]
        data = docs.retrieve(body["query"])
    except KeyError:
        return {"error": "No documents processed yet"}, 404

    return {"results": data}, 200, {"X-Connector-Id": app.config.get("APP_ID")}


def process(body):
    demo_store["docs"] = Documents(body["sources"])

    return {"message": "Documents processed successfully"}, 200


# This function is run for all endpoints to ensure requests are using a valid API key
def apikey_auth(token):
    if token != app.config.get("CONNECTOR_API_KEY"):
        raise Unauthorized()
    # successfully authenticated
    return {}
