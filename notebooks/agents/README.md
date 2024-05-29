## Overview

You will find a collection of notebooks that demonstrate how to build `agents` with Cohere.

## Notebooks

### API
The following notebooks exclusively use the Cohere API to call tools.

1. [Tool Use](Tool_Use.ipynb): A minimal working example of how to use our chat API to call tools.
2. [Tool Use Configuration](Vanilla_Tool_Use.ipynb): A simple walkthrough of how to configure the chat API to reason over tools that call a mock API.
3. [Native Financial CSV Agent](financial-csv-agent/financial_csv_publication_native.ipynb): This notebook demonstrates how to setup a Cohere Native API sequence of tool calls to answer questions over the income statement and balance sheet from Apple’s SEC10K 2020 form.

### Langchain
The following notebooks use the cohere_react_agent in Langchain which is currently the recommended way to build multi-step reasoning Agents with Cohere.

1. [Multi Step Tool Use](Multi_Step_Tool_Use.ipynb): this is a simple tutorial example, of how to use Langchain `cohere_react_agent` to run multi-step RAG.
2. [Data Science Agent](Vanilla_Multi_Step_Tool_Use.ipynb): this is a detailed walkthrough of how to use Langchain `cohere_react_agent` to build a basic data science agent.
3. [Agent Memory](agent_memory_walkthrough.ipynb): A walkthrough of how to use Langchain cohere_react_agent to effectively manage short term chat history that contains tool calls with Langchain.
3. [Agent API Calls](agents_with_deterministic_functions.ipynb): A walkthrough of how to use Langchain cohere_react_agent to make API calls to external services that require regex.
4. [Financial CSV Agent](financial-csv-agent/financial_csv_publication.ipynb): A walkthrough of how to use Langchain cohere_react_agent to read and process CSV files using a python tool.
5. [Agentic RAG](agentic-RAG/agentic_rag_publication.ipynb): A walkthrough of how to use Langchain cohere_react_agent to run RAG as an agent tool to handle PDFs with mixed table and text data.
6. [Financial CSV Agent](financial-csv-agent/financial_csv_publication.ipynb): This notebook demonstrates how to setup a Langchain Cohere ReAct Agent to answer questions over the income statement and balance sheet from Apple’s SEC10K 2020 form.
7. [SQL Agent](sql_agent/sql_agent.ipynb): In this notebook we explore how to setup a Cohere ReAct Agent to answer questions over SQL Databases using Langchain’s existing SQLDBToolkit.
