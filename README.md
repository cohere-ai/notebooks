# Cohere Examples

Welcome! This repository provides a collection of examples to help you build LLM-powered applications with the [Cohere API](https://docs.cohere.com/). They contain step-by-step guides, with code examples and explanations, to help you understand and use the API effectively.

The examples are grouped into 3 categories:
1. **[Getting started](#getting-started)**: A Cohere 101 guide. Build your first Cohere application – an onboarding assistant for new hires.
2. **[LLM University](#llm-university)**: The code companion to the [LLM University](https://cohere.com/llmu) course containing a comprehensive list of modules.
3. **[Cookbook](#cookbook)**: Deep dive into various techniques in the following topics: [RAG](#rag), [Agents](#agents), [Search & embeddings](#search-and-embeddings), [Summarization](#summarization), and [Others](#others)

Interested to contribute? Read the [contributing guide](#contributing).

<br>

## Quick Start

### Installation
```bash
# Install the Cohere Python SDK
pip install cohere

# Clone this repository
git clone https://github.com/cohere-ai/notebooks.git
cd notebooks
```

### Authentication
```python
import cohere
co = cohere.Client('your-api-key')  # Get your API key from dashboard.cohere.ai
```

## Prerequisites
- Python 3.7 or higher
- A Cohere API key ([Sign up here](https://dashboard.cohere.ai))
- Familiarity with Jupyter notebooks

## Getting Started
This is a Cohere 101 guide. Build your first Cohere application: An onboarding assistant for new hires.
Duration: ~15 mins.

| Title                                                 | Colab |
|-------------------------------------------------------|-------|
| [Part 1: Installation and setup](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/getting-started/tutorial_pt1.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/getting-started/tutorial_pt1.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| [Part 2: Text generation](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/getting-started/tutorial_pt2.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/getting-started/tutorial_pt2.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| [Part 3: Chatbots](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/getting-started/tutorial_pt3.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/getting-started/tutorial_pt3.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| [Part 4: Semantic search](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/getting-started/tutorial_pt4.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/getting-started/tutorial_pt4.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| [Part 5: Reranking](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/getting-started/tutorial_pt5.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/getting-started/tutorial_pt5.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| [Part 6: Retrieval-augmented generation \(RAG\)](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/getting-started/tutorial_pt6.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/getting-started/tutorial_pt6.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| [Part 7: Agents with tool use](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/getting-started/tutorial_pt7.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/getting-started/tutorial_pt7.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |

<br>

## LLM University
This section contains the code companion to the [LLM University](https://cohere.com/llmu) course containing a comprehensive list of modules.

| Module | Title | Colab |
|---|---|---|
| What are Large Language Models? | [Similarity Between Words and Sentences](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/What_Is_Similarity_Between_Sentences.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/What_Is_Similarity_Between_Sentences.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| Text Representation | [Introduction to Text Embeddings, Semantic Search, and Clustering](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/Introduction_Text_Embeddings.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/Introduction_Text_Embeddings.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| | [Topic Modeling](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/Analyzing_Hacker_News_with_Six_Language_Understanding_Methods.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/Analyzing_Hacker_News_with_Six_Language_Understanding_Methods.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| | [Few-Shot Classification](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/Classify_Endpoint.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/Classify_Endpoint.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| | [Fine-Tuning for Classification](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/Fine_Tuning_for_Classify.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/Fine_Tuning_for_Classify.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| Text Generation | [Building a Chatbot](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/Building_a_Chatbot.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/Building_a_Chatbot.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| | [Parameters for Controlling Outputs](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/Parameters_for_Controlling_Outputs.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/Parameters_for_Controlling_Outputs.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| | [Prompt Engineering Basics](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/Prompt_Engineering_Basics.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/Prompt_Engineering_Basics.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| | [Fine-Tuning for Chat](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/Fine_Tuning_for_Chat.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/Fine_Tuning_for_Chat.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| Deployment | [Deploying with Streamlit](https://github.com/cohere-ai/notebooks/tree/main/notebooks/llmu/examples/deploy_streamlit) |  N/A   |
|            | [Deploying with FastAPI](https://github.com/cohere-ai/notebooks/tree/main/notebooks/llmu/examples/deploy_fastapi) |  N/A   |
|            | [Deploying on Google Sheets with Google Apps Script](https://github.com/cohere-ai/notebooks/tree/main/notebooks/llmu/examples/deploy_google_apps_script) |  N/A    |
|            | [Deploying as a Chrome Extension](https://github.com/cohere-ai/sandbox-condense) | N/A     |
| Semantic Search | [What is Semantic Search?](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/What_is_Semantic_Search.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/What_is_Semantic_Search.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| | [Keyword Search, Dense Retrieval, Reranking, and Generating Answers](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/End_To_End_Wikipedia_Search.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/End_To_End_Wikipedia_Search.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| Prompt Engineering | [Constructing Prompts](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/Constructing_Prompt_Commands.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/Constructing_Prompt_Commands.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| | [Use Case Patterns](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/Command_Model_Use_Case_Patterns.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/Command_Model_Use_Case_Patterns.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| | [Validating Outputs](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/Validating_Large_Language_Model_Outputs.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/Validating_Large_Language_Model_Outputs.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| Retrieval-Augmented Generation (RAG) | [Getting Started with RAG](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/Introduction_to_RAG.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/Introduction_to_RAG.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| | [RAG with Chat, Embed, and Rerank](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/RAG_with_Chat_Embed_and_Rerank.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/RAG_with_Chat_Embed_and_Rerank.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| | [RAG with Connectors](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/RAG_with_Connectors.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/RAG_with_Connectors.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| | [RAG with Quickstart Connectors](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/RAG_with_Quickstart_Connectors.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/RAG_with_Quickstart_Connectors.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| | [RAG over Large-Scale Data](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/RAG_over_Large_Scale_Data.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/RAG_over_Large_Scale_Data.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| Tool Use | [Tool Use Anatomy](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/tool_use_anatomy.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/tool_use_anatomy.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| | [Single-Step Tool Use](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/single_step_tool_use.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/single_step_tool_use.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| | [Multi-Step Tool Use](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/multi_step_tool_use.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/multi_step_tool_use.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| | [Tool Use with LangChain](https://github.com/cohere-ai/notebooks/blob/main/notebooks/agents/Data_Analyst_Agent_Cohere_and_Langchain.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/agents/Data_Analyst_Agent_Cohere_and_Langchain.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| Cohere on AWS | [Text generation on Bedrock](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/co_aws_ch3_text_generation.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/co_aws_ch3_text_generation.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
|  | [Semantic search on Bedrock](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/co_aws_ch4_semantic_search.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/co_aws_ch4_semantic_search.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
|  | [Reranking on SageMaker](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/co_aws_ch5_rerank_sm.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/co_aws_ch5_rerank_sm.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
|  | [RAG on Bedrock and SageMaker](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/co_aws_ch6_rag_bedrock_sm.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/co_aws_ch6_rag_bedrock_sm.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
|  | [Tool use on Bedrock](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/co_aws_ch7_tool_use.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/co_aws_ch7_tool_use.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
|  | [Fine-tuning on Bedrock/SageMaker](https://github.com/cohere-ai/notebooks/blob/main/notebooks/llmu/co_aws_ch8_ft_command.ipynb) | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/llmu/co_aws_ch8_ft_command.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |

<br>

## Cookbook
This section provides a deep dive into various techniques in the following topics:
- [RAG](#rag)
- [Agents](#agents)
- [Search & embeddings](#search-and-embeddings)
- [Summarization](#summarization)
- [Others](#others)


<br>

### RAG
| Title | Components | Colab |
|--------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [Basic RAG](https://github.com/cohere-ai/notebooks/blob/main/notebooks/Vanilla_RAG.ipynb) | Chat, Embed, Rerank | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>](https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/Vanilla_RAG.ipynb) |
| [End-to-end RAG using Elasticsearch and Cohere](https://github.com/cohere-ai/notebooks/blob/main/notebooks/Cohere_Elastic_Guide.ipynb) | Chat, Embed, Rerank, Elasticsearch | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>](https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/Cohere_Elastic_Guide.ipynb) |
| [Chunking Strategies](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/Chunking_strategies.ipynb) | Chat, Embed, Rerank, LlamaIndex, LangChain | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>](https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/Chunking_strategies.ipynb) |
| [Migrating Monolithic Prompts to Command-R with RAG](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/Migrating_Monolithic_Prompts_to_Command_R_with_RAG.ipynb) | Chat | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>](https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/Migrating_Monolithic_Prompts_to_Command_R_with_RAG.ipynb) |
| [RAG With Chat Embed and Rerank via Pinecone](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/RAG_with_Chat_Embed_and_Rerank_via_Pinecone.ipynb) | Chat, Embed, Rerank, Pinecone | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>](https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/RAG_with_Chat_Embed_and_Rerank_via_Pinecone.ipynb) |
| [Creating a QA Bot From Technical Documentation](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/Creating_a_QA_bot_from_technical_documentation.ipynb) | Chat, Embed, Rerank, LlamaIndex | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>](https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/Creating_a_QA_bot_from_technical_documentation.ipynb) |
| [Analysis of Form 10-K/10-Q Using Cohere and RAG](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/Analysis_of_Form_10_K_Using_Cohere_and_RAG.ipynb) | Cohere, Embed, Rerank, LlamaIndex, Langchain | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>](https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/Analysis_of_Form_10_K_Using_Cohere_and_RAG.ipynb) |
| [Adaptive RAG](https://github.com/cohere-ai/notebooks/blob/main/notebooks/agents/Multi_Step_Tool_Use.ipynb) | Chat, LangChain | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>](https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/agents/Multi_Step_Tool_Use.ipynb) |


### Agents

| Title | Components | Colab |
|--------------------------------------------------------------|--------------------------------|-----------------|
| [Basic Tool Use](https://github.com/cohere-ai/notebooks/blob/main/notebooks/agents/Vanilla_Tool_Use.ipynb) | Chat                           | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/agents/Vanilla_Tool_Use.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Multi-Step Tool Use](https://github.com/cohere-ai/notebooks/blob/main/notebooks/agents/Vanilla_Multi_Step_Tool_Use.ipynb) | Chat, Embed, LangChain         |<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/agents/Vanilla_Multi_Step_Tool_Use.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Calendar Agent with Native Multi Step Tool](https://github.com/cohere-ai/notebooks/blob/main/notebooks/agents/Tool_Use.ipynb) | Chat                           | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/agents/Tool_Use.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [A Data Analyst Agent Built with Cohere and Langchain](https://github.com/cohere-ai/notebooks/blob/main/notebooks/agents/Data_Analyst_Agent_Cohere_and_Langchain.ipynb) | Chat, LangChain                |<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/agents/Data_Analyst_Agent_Cohere_and_Langchain.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Short-Term Memory Handling for Agents](https://github.com/cohere-ai/notebooks/blob/main/notebooks/agents/agent_memory_walkthrough.ipynb) | Chat, LangChain                |<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/agents/agent_memory_walkthrough.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Agent API Calls](https://github.com/cohere-ai/notebooks/blob/main/notebooks/agents/agents_with_deterministic_functions.ipynb) | Chat, LangChain                |<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/agents/agents_with_deterministic_functions.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Financial CSV Agent with Langchain](https://github.com/cohere-ai/notebooks/blob/main/notebooks/agents/financial-csv-agent/financial_csv_publication.ipynb) | Chat, LangChain                |<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/agents/financial-csv-agent/financial_csv_publication.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Agentic RAG for PDFs with mixed data](https://github.com/cohere-ai/notebooks/blob/main/notebooks/agents/agentic-RAG/agentic_rag_langchain.ipynb) | Chat, Embed, Rerank, LangChain |<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/agents/agentic-RAG/agentic_rag_langchain.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [SQL Agent](https://github.com/cohere-ai/notebooks/blob/main/notebooks/agents/sql_agent/sql_agent.ipynb) | Chat, LangChain                |<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/agents/sql_agent/sql_agent.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Financial CSV Agent with Native Multi-Step Cohere API](https://github.com/cohere-ai/notebooks/blob/main/notebooks/agents/financial-csv-agent/financial_csv_publication_native.ipynb) | Chat, LangChain                |<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/agents/financial-csv-agent/financial_csv_publication_native.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [PDF Extractor with Native Multi Step Tool Use](https://github.com/cohere-ai/notebooks/blob/main/notebooks/agents/pdf-extractor/pdf_extractor.ipynb)<br> | Chat, Unstructured             |<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/agents/pdf-extractor/pdf_extractor.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Agentic Multi-Stage RAG with Cohere Tools API](https://github.com/cohere-ai/notebooks/blob/main/notebooks/agents/agentic-RAG/agentic_multi_stage_rag_native.ipynb) | Chat, Embed                    |<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/agents/agentic-RAG/agentic_multi_stage_rag_native.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Agentic RAG with an Evaluator, Web Search, Human Input, and Python Tool](https://github.com/cohere-ai/notebooks/blob/main/notebooks/agents/agentic-RAG/multi_purpose_agent.ipynb) | Chat, Embed, LangChain         |<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/agents/agentic-RAG/multi_purpose_agent.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
## Search and Embeddings
| Title                                                | Components      | Colab |
|--------------------------------------------------------------|-----------------|------------------------------------------------------------------------|
| [Basic Semantic Search](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/Basic_Semantic_Search.ipynb) | Embed           | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/Basic_Semantic_Search.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Basic Reranking](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/rerank-demo.ipynb) | Rerank          | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/rerank-demo.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Wikipedia Semantic Search with Cohere Embedding Archives](https://github.com/cohere-ai/notebooks/blob/main/notebooks/Wikipedia_Semantic_Search_With_Cohere_Embeddings_Archives.ipynb) | Embed           | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/Wikipedia_Semantic_Search_With_Cohere_Embeddings_Archives.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Semantic Search with Cohere Embed Jobs and Pinecone serverless Solution](https://github.com/cohere-ai/notebooks/blob/main/notebooks/Embed_Jobs_Serverless_Pinecone_Semantic_Search.ipynb) | Embed, Pinecone | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/Embed_Jobs_Serverless_Pinecone_Semantic_Search.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Semantic Search with Cohere Embed Jobs](https://github.com/cohere-ai/notebooks/blob/main/notebooks/Embed_Jobs_Semantic_Search.ipynb) | Embed, Rerank   | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/Embed_Jobs_Semantic_Search.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Wikipedia Semantic Search with Cohere + Weaviate](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/Wikipedia_search_demo_cohere_weaviate.ipynb) | Embed, Weaviate | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/Wikipedia_search_demo_cohere_weaviate.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |


### Summarization
| Title                                              | Components      | Colab |
|--------------------------------------------------------------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Long Form General Strategies](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/Long_form_General_Strategies.ipynb) | Chat, Embed, Rerank | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/Long_form_General_Strategies.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> </a> |
| [Summarization Evals](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/Summarization_Evals.ipynb) | Chat                | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/Summarization_Evals.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> </a> |
| [Grounded Summarization Using Command R](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/Grounded_summarisation_using_Command_R.ipynb) | Chat, Embed         | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/Grounded_summarisation_using_Command_R.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> </a> |


### Others
| Title | Components | Colab |
|--------------------------------------------------------------|-----------------------|------------------------------------------------------------------------|
| [Advanced Document Parsing For Enterprises](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/Document_Parsing_For_Enterprises.ipynb) | Chat, Embed, Rerank | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/Document_Parsing_For_Enterprises.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Analyzing Hacker News with Six Language Understanding Methods](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/Analyzing_Hacker_News_with_Six_Language_Understanding_Methods.ipynb) | Embed | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/Analyzing_Hacker_News_with_Six_Language_Understanding_Methods.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Text Classification Using Embeddings](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/Text_Classification_Using_Embeddings.ipynb) | Embed | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/Text_Classification_Using_Embeddings.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Article Recommender with Text Embedding Classification Extraction](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/Article_Recommender_with_Text_Embedding_Classification_Extraction.ipynb) | Chat, Embed, Classify | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/Article_Recommender_with_Text_Embedding_Classification_Extraction.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Fueling Generative Content with Keyword Research](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/Fueling_Generative_Content_with_Keyword_Research.ipynb) | Chat, Embed | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/Fueling_Generative_Content_with_Keyword_Research.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [Topic Modeling AI Papers](https://github.com/cohere-ai/notebooks/blob/main/notebooks/guides/Topic_Modeling_AI_Papers.ipynb) | Embed | <a target="_blank" href="https://colab.research.google.com/github/cohere-ai/notebooks/blob/main/notebooks/guides/Topic_Modeling_AI_Papers.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |

<br>

## Contributing
Thank you for your interest in contributing! We appreciate your input and encourage you to share your ideas and improvements. Here are some ways you can contribute:

- New Examples and Guides: If you have an idea for a new example or guide, please share it with us! Create an issue to discuss your proposal, gather feedback, and get started. This ensures your contribution aligns with the project's scope and avoids duplication.

- Improvements and Updates: You can contribute by enhancing existing examples and guides. This could involve adding more detailed explanations, code snippets, error handling, or exploring advanced usage. Your insights and expertise will make our examples more useful.

- Feedback and Suggestions: Your feedback is invaluable. If you have suggestions for improving the structure, content, or overall user experience of this repository, please create an issue or contact us directly. We want to ensure this resource is as helpful as possible.

Please review existing issues and pull requests before starting your contribution to avoid duplication of efforts. We value your unique insights and contributions, and we want to ensure they are well-aligned with the project's goals. 

Thank you for your contributions and for helping to make this repository a valuable resource for the developer community!
