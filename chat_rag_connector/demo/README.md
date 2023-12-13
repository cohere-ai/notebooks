# Template Quick Start Connector

This is a _template_ for a simple quick start connector that return static data. This can serve as starting point for creating a brand new connector.

## Configuration

This connector is very simple and only needs a `TEMPLATE_CONNECTOR_API_KEY` environment variable to be set. This value will be used for bearer token authentication to protect this connector from abuse.

A `.env-template` file is provided with all the environment variables that are used by this connector.

## Development

Create a virtual environment and install dependencies with poetry. We recommend using in-project virtual environments:

```bash
  $ poetry config virtualenvs.in-project true
  $ poetry install --no-root
```

Then start the server

```bash
  $ poetry run flask --app provider --debug run --port 5000
```

and check with curl to see that everything is working

```bash
  $ curl --request POST \
    --url http://localhost:5000/search \
    --header 'Content-Type: application/json' \
    --data '{
    "query": "which species of penguin is the tallest?"
  }'
```

Alternatively, load up the Swagger UI and try out the API from a browser: http://localhost:5000/ui/
