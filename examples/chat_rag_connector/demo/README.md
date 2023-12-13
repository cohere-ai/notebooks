# LLM University - Chat and RAG with Connectors

This is the code used in the LLM University chapter on [Chat and RAG with connectors](https://txt.cohere.com/rag-chatbot-connector/)


It is created based on the quick start connector template available on the quickstart connectors [repository](https://github.com/cohere-ai/quick-start-connectors/tree/main/_template_).

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
