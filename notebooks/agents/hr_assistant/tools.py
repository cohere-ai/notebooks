import datetime
import os

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.agents import Tool
from langchain_experimental.utilities import PythonREPL
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.tools.tavily_search import TavilySearchResults
import pandas as pd
import pytz

load_dotenv()

cohere_api_key = os.getenv("CO_API_KEY")

### TOOLS ###

# ----------- python interpreter -----------
python_repl = PythonREPL()
python_tool = Tool(
    name="python_repl",
    description="""Executes python code and returns the result. The code runs in a static sandbox without interactive mode, so any output needed later should be printed or saved to a file. Useful for math - i.e. addition, subtraction, multiplication, division, or other operations.""",
    func=python_repl.run,
)
python_tool.name = "python_tool"

class ToolInput(BaseModel):
    code: str = Field(description="Python code to execute.")

python_tool.args_schema = ToolInput


# ----------- get_info_employee -----------
@tool
def get_info_employee(employee):
    """Find and retrieve information about a specific employee. The following attributes are available:
    
- name: the name of the employee
- used_days_off: how many vacation days they have used this year
- location: the location of the employee
- role: the role of the employee
    """

    df = pd.read_csv('employees.csv')
    df = df.loc[df['name'] == employee]
    return df.to_dict('records')[0]

class get_info_employee_inputs(BaseModel):
    employee: str = Field(description="the name of the employee")

get_info_employee.name = "get_info_employee"
get_info_employee.description = """Find and retrieve information about a specific employee. The following attributes are available:
    
- name: the name of the employee
- used_days_off: how many vacation days they have used this year
- location: the location of the employee
- role: the role of the employee"""
get_info_employee.args_schema = get_info_employee_inputs

# ----------- search_cohere_policies -----------
@tool
def search_cohere_policies(query):
    """Run a query against a database to retrieve potentially relevant documents about HR policies at Cohere."""
    # documents = open('cohere_public_data.txt').read().split('*****')
    cohere_embedder = CohereEmbeddings(cohere_api_key=cohere_api_key)
    vectorstore = Chroma(collection_name="cohere_public_data", persist_directory="embs_cohere_public_data", embedding_function=cohere_embedder)
    retriever = vectorstore.as_retriever()
    txt = retriever.invoke(query)[0].page_content
    return txt

class search_cohere_policies_inputs(BaseModel):
    query: str = Field(description="the query to use to retrieve relevant documents.")

search_cohere_policies.name = "search_cohere_policies"
search_cohere_policies.description = "Run a query against a database to retreive relevant documents about HR policies at Cohere."
search_cohere_policies.args_schema = search_cohere_policies_inputs

# ----------- internet_search -----------
# os.environ["TAVILY_API_KEY"] = ""
internet_search = TavilySearchResults()

class TavilySearchInput(BaseModel):
    query: str = Field(description="Query to search the Internet with")

internet_search.args_schema = TavilySearchInput
internet_search.name = "internet_search"
internet_search.description = "Returns a list of relevant document snippets for a textual query retrieved from the internet."


# ----------- get_employee_timezone -----------
@tool
def get_location_utc_offset(city):
    """Find and retrieve current UTC offset for a city. 
    """
    # we constrain the options to the below for simplicity
    location_tz_map = {
        "New York": "America/New_York",
        "Toronto": "America/Toronto",
        "Berlin": "Europe/Berlin",
        "London": "Europe/London",
        "Paris": "Europe/Paris",
        "Hong Kong": "Asia/Hong_Kong",
        "Tokyo": "Asia/Tokyo",
        "Singapore": "Asia/Singapore",
        "Sydney": "Australia/Sydney"
    }

    location_tz = location_tz_map[city]
    current_time = datetime.datetime.now(pytz.timezone(location_tz))

    return current_time.utcoffset().total_seconds() / 3600

class get_location_utc_offset_inputs(BaseModel):
    city: str = Field(description="name of city to retrieve timezone for. One of `New York`, `Toronto`, `Berlin`, `London`, `Paris`, `Hong Kong`, `Tokyo`, `Singapore`, `Sydney`.")

get_location_utc_offset.name = "get_employee_timezone"
get_location_utc_offset.description = "Find and retrieve current UTC offset for a city. "
get_location_utc_offset.args_schema = get_location_utc_offset_inputs

# ----------- get_template -----------
@tool
def get_template(template_type):
    """Returns a template for different kinds of communications indicated by the query. Possible template types are:

- offer: an offer letter template for a job application
- rejection: a rejection letter template for a job application

All template values are in square brackets. These are the template values for the `offer` template:

[Candidate Name]: the name of the candidate
[Role]: the role in question
[Desired Start Date]: the desired start date for the candidate
[Offered Salary]: the salary offered to the candidate
[Location]: the location of the job

These are the template values for the `rejection` template:
[Candidate Name]: the name of the candidate
[Role]: the role in question
"""

    template_dict = {
        'offer': """Dear [Candidate Name], 

I am delighted to extend an offer for the position of [Role] at Cohere. Your expertise and passion for machine learning have impressed us, and we strongly believe that you will be an invaluable addition to our team. 

At Cohere, we are dedicated to pushing the boundaries of machine learning technology and innovating in the field. As a key member of our team, you will play a pivotal role in driving this mission forward. Your responsibilities will include designing and developing machine learning models, collaborating with cross-functional teams, and contributing to cutting-edge research and development initiatives. 

Here are the details of our offer: 
1. Job Title: [Role]
2. Start Date: [Desired Start Date] (negotiable)
3. Salary: [Offered Salary] (annual, semi-annual, or monthly basis)
4. Benefits: 
   - Health insurance coverage, including medical, dental, and vision benefits.
   - Retirement plan options, such as a 401(k) or similar, with employer matching contributions up to a certain percentage.
   - Professional development budget for conferences, courses, or certifications to support your continued growth in the field.
5. Bonus and Incentives: 
   - Performance-based bonus structure
   - Equity options/grants, offering the opportunity to benefit from the company's success and growth.
6. Work Location: [Location] 

We are confident that you will find our company culture stimulating and rewarding. We value collaboration, continuous learning, and a healthy work-life balance. You will be joining a dynamic and supportive team that is excited to welcome you aboard. 

We are thrilled at the prospect of having you join our team and contributing your exceptional skills and knowledge to our organization. Congratulations, and we look forward to hearing back from you soon! 

Sincerely,  
Cohere""",
        'rejection': """Dear [Candidate Name], 

Thank you for your interest in the [Role] position at Cohere. I appreciate the time and effort you invested in applying and participating in our hiring process. 

After careful consideration and a thorough evaluation of your qualifications, I regret to inform you that we have decided to pursue other candidates for this role. The competition was intense, and we had the challenging task of selecting from a pool of talented applicants. 

Please know that this decision in no way reflects your capabilities or potential as a [Role]. Our decision was based on specific requirements and needs for this particular role within our team dynamics. I encourage you to stay resilient and confident in your skills as you continue your job search. 

I wish you the very best of luck in your future endeavors, and I have no doubt that you will find a suitable position where your expertise will be valued and appreciated. 

Sincerely,  
Cohere"""
    }

    return template_dict.get(template_type, "")

class get_template_inputs(BaseModel):
    template_type: str = Field(description="the template category to retrieve relevant template for. One of `offer` or `rejection`.")

get_template.name = "get_template"
get_template.description = "Return the specific template for different kinds of communications."
get_template.args_schema = get_template_inputs