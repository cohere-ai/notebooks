import logging
import os

import connexion  # type: ignore
from dotenv import load_dotenv

load_dotenv()

API_VERSION = "api.yaml"


class UpstreamProviderError(Exception):
    def __init__(self, message) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


def create_app() -> connexion.FlaskApp:
    # use connexion to create a flask app with the endpoints defined in api.yaml spec
    app = connexion.FlaskApp(__name__, specification_dir="../.openapi")
    app.add_api(
        API_VERSION, resolver=connexion.resolver.RelativeResolver("provider.app")
    )
    logging.basicConfig(level=logging.INFO)
    flask_app = app.app
    # load environment variables prefixed with the name of the current directory
    config_prefix = os.path.split(os.getcwd())[1].upper().replace("_", "")
    flask_app.config.from_prefixed_env(config_prefix)
    flask_app.config["APP_ID"] = config_prefix
    return flask_app
