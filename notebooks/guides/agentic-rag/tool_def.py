from langchain.agents import Tool
from langchain_community.tools.tavily_search import TavilySearchResults
from pydantic import BaseModel, Field
from langchain_experimental.utilities import PythonREPL
from typing import Dict, List, Optional


def search_developer_docs(query: str) -> dict:
    
    developer_docs = [{"text" : "## The Rerank endpoint\nThis endpoint takes in a query and a list of texts and produces an ordered array with each text assigned a relevance score."},
    
    {"text" : "## The Embed endpoint\nThis endpoint returns text embeddings. An embedding is a list of floating point numbers that captures semantic information about the text that it represents.."},

    {"text" : "## Embed endpoint multilingual support\nIn addition to embed-english-v3.0 we offer a best-in-class multilingual model embed-multilingual-v3.0 with support for over 100 languages."},
    
    {"text" : "## The Chat endpoint\nThis endpoint facilitates a conversational interface, allowing users to send messages to the model and receive text responses."},
    
    {"text" : "## Retrieval Augmented Generation (RAG)\nRAG is a method for generating text using additional information fetched from an external data source, which can greatly increase the accuracy of the response."},
    
    {"text" : "## The temperature parameter\nTemperature is a number used to tune the degree of randomness of a generated text."},
    ]

    return developer_docs
    
def search_internet(query: str) -> dict:
    tool = TavilySearchResults(
        max_results=5,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=True
    )
    documents = tool.invoke({"query": query})
    
    return documents

def search_code_examples(query: str) -> dict:
    
    code_examples = [
        {"content": "Calendar Agent with Native Multi Step Tool"},
        {"content": "Wikipedia Semantic Search with Cohere Embedding Archives"},
        {"content": "RAG With Chat Embed and Rerank via Pinecone"},
        {"content": "Build Chatbots That Know Your Business with MongoDB and Cohere"},
        {"content": "Advanced Document Parsing For Enterprises"}
    ]
    
    return code_examples

def search_code_examples_detailed(query: str = None, programming_language: Optional[str] = None, endpoints: Optional[List[str]] = None) -> dict:
    
    code_examples = [
        {"content": "Calendar Agent with Native Multi Step Tool", "programming_language": "py", "endpoints": ["chat"]},
        {"content": "Wikipedia Semantic Search with Cohere Embedding Archives", "programming_language": "py", "endpoints": ["embed", "rerank"]},
        {"content": "RAG With Chat Embed and Rerank via Pinecone", "programming_language": "py", "endpoints": ["chat", "embed", "rerank"]},
        {"content": "Build Chatbots That Know Your Business with MongoDB and Cohere", "programming_language": "py", "endpoints": ["chat", "embed", "rerank"]},
        {"content": "Advanced Document Parsing For Enterprises", "programming_language": "py", "endpoints": ["embed"]},
        {"content": "Build a Chrome extension to summarize web pages", "programming_language": "js", "endpoints": ["chat"]},
        {"content": "Sentiment analysis using Google Apps Script", "programming_language": "js", "endpoints": ["classify"]},
    ]
    
    # Filter based on file_type if provided
    if programming_language:
        filtered_examples = [ex for ex in code_examples if any(lang in ex["programming_language"] for lang in programming_language)]
    
    # Filter based on endpoints if provided
    elif endpoints:
        filtered_examples = [ex for ex in code_examples if any(endpoint in ex["endpoints"] for endpoint in endpoints)]
    
    else:
        filtered_examples = code_examples
                             
    return filtered_examples


python_repl = PythonREPL()
python_tool = Tool(
    name="python_repl",
    description="Executes python code and returns the result. The code runs in a static sandbox without interactive mode, so print output or save output to a file.",
    func=python_repl.run,
)
python_tool.name = "python_interpreter"


class ToolInput(BaseModel):
    code: str = Field(description="Python code to execute.")
    
    
python_tool.args_schema = ToolInput


def analyze_evaluation_results(code: str) -> dict:
    """
    Function to run given python code
    """
    input_code = ToolInput(code=code)
    
    python_answer = python_tool.func(input_code.code)
    
    return python_answer


search_developer_docs_tool = {
        "type": "function",
        "function": {
            "name": "search_developer_docs",
            "description": "Searches the Cohere developer documentation. Use this tool for queries related to the Cohere API, SDKs, or other developer resources.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query."
                    }
                },
                "required": ["query"]
            }
        }
}
    
search_internet_tool = {
        "type": "function",
        "function": {
            "name": "search_internet",
            "description": "Searches the internet. Use this tool for general queries that would not be found in the developer documentation.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query."
                    }
                },
                "required": ["query"]
            }
        }
}

search_code_examples_tool = {
        "type": "function",
        "function": {
            "name": "search_code_examples",
            "description": "Searches code examples and tutorials on using Cohere.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query."
                    }
                },
                "required": ["query"]
            }
        }
}


search_code_examples_detailed_tool = {
        "type": "function",
        "function": {
            "name": "search_code_examples_detailed",
            "description": "Searches code examples or tutorials of using Cohere.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query."
                    },
                    "programming_language": {
                        "type": "string",
                        "description": "The programming language of the code example or tutorial. Only use this property when specified by the user. Possible enum values: py, js."
                    },
                    "endpoints": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "The Cohere endpoints used in the code example or tutorial. Only use this property when asked by the user. Possible enum values: chat, embed, rerank, classify."
                    }
                },
                "required": ["query"]
            }
        }
}

analyze_evaluation_results_tool = {
        "type": "function",
        "function": {
            "name": "analyze_evaluation_results",
            "description": "Generate Python code using the pandas library to analyze evaluation results from a dataframe called `evaluation_results`. The dataframe has columns 'usecase','run','score','temperature','tokens', and 'latency'. You must start with `import pandas as pd` and read a CSV file called `evaluation_results.csv` into the `evaluation_results` dataframe.",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "Executable Python code"
                    }
                },
                "required": ["code"]
            }
        }
}