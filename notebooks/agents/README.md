## Overview

You will find a collection of notebooks that demonstrate how to build `agents` with Cohere.

## Notebooks
There are a number of ways to build agents with Cohere. The following notebooks demonstrate how to build agents using the native Cohere API which involves handling tool and API calls, as well as how to build agents with Langchain's [cohere_react_agent](https://github.com/langchain-ai/langchain-cohere/blob/main/libs/cohere/langchain_cohere/react_multi_hop/agent.py).

### Native API Cookbooks
The following notebooks exclusively use the Cohere API to call tools.

1. [Single Step Tool Use](Tool_Use.ipynb): A minimal working example of how to use our chat API to call tools.
2. [Tool Use Configuration](Vanilla_Tool_Use.ipynb): A simple walkthrough of how to configure the chat API to reason over tools that call a mock API.
3. [Native Financial CSV Agent](financial-csv-agent/financial_csv_publication_native.ipynb): This notebook demonstrates how to setup a Cohere Native API sequence of tool calls to answer questions over the income statement and balance sheet from Apple’s SEC10K 2020 form.

### Langchain Agent Cookbooks
The following notebooks use the cohere_react_agent in Langchain which is currently the recommended way to build multi-step reasoning Agents with Cohere.

1. [Multi Step Tool Use](Vanilla_Multi_Step_Tool_Use.ipynb): this is a simple tutorial example, of how to use Langchain `cohere_react_agent` to run multi-step tool calls.
2. [Adaptive RAG](Multi_Step_Tool_Use.ipynb): this is a tutorial of how to use Langchain `cohere_react_agent` to run adaptive RAG analysis on financial documents.
3. [Data Science Agent](Data_Analyst_Agent_Cohere_and_Langchain.ipynb): this is a detailed walkthrough of how to use Langchain `cohere_react_agent` to build a basic data science agent.
4. [Agent Memory](agent_memory_walkthrough.ipynb): A walkthrough of how to use Langchain cohere_react_agent to effectively manage short term chat history that contains tool calls with Langchain.
5. [Agent API Calls](agents_with_deterministic_functions.ipynb): A walkthrough of how to use Langchain cohere_react_agent to make API calls to external services that require regex.
6. [Financial CSV Agent](financial-csv-agent/financial_csv_publication.ipynb): A walkthrough of how to use Langchain cohere_react_agent to read and process CSV files using a python tool.
7. [Agentic RAG for PDFs with mixed data](agentic-RAG/agentic_rag_publication.ipynb): A walkthrough of how to use Langchain cohere_react_agent to run RAG as an agent tool to handle PDFs with mixed table and text data.
8. [Financial CSV Agent](financial-csv-agent/financial_csv_publication.ipynb): This notebook demonstrates how to setup a Langchain Cohere ReAct Agent to answer questions over the income statement and balance sheet from Apple’s SEC10K 2020 form.
9. [SQL Agent](sql_agent/sql_agent.ipynb): In this notebook we explore how to setup a Cohere ReAct Agent to answer questions over SQL Databases using Langchain’s existing SQLDBToolkit.


We will continue to introduce more examples to help you get started with building agents using Cohere.
