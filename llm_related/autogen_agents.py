# pip install pyautogen
import os
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
from dotenv import load_dotenv


load_dotenv()
# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample.json
config_list = [
    {
        "model": "gpt-4",
        "api_key":  os.getenv("OPENAI_API_KEY")
    },
    {
        "model": "gpt-3.5-turbo",
        "api_key": os.getenv("OPENAI_API_KEY"),
        "api_version": "2023-03-01-preview"
    }
]

llm_config_json = {
        "timeout": 600,
        "cache_seed": 42,
        "config_list": config_list,
        "temperature": 0,
    }
# config_list = config_list_from_json(env_or_file="config_list_from_dotenv")
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})
user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")
# This initiates an automated chat between the two agents to solve the task


## Example 2: Research survey
import autogen
config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",  # filename
    filter_dict={"model": ["gpt-3.5-turbo"]}, # use only this model(s)
    # filter_dict={"model": ["gpt-4-32k"]}, # use only this model(s)
)
llm_config = {
    "timeout": 600,
    "cache_seed": 44,  # change the seed for different trials
    "config_list": config_list,
    "temperature": 0,
}
# create an AssistantAgent instance named "assistant"
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
    is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,
)
# create a UserProxyAgent instance named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,
    max_consecutive_auto_reply=10,
    code_execution_config={
        "work_dir": "work_dir",
        "use_docker": False,
    },
)

task_extra = """
You are hustle bot, a bot devilering specific ideas how to make money given an investment. We have 5000 Euros to invest and we are software developers and engineers so we can set up websites or develop any tech stack. Come up with a detailed plan how we should invest our time and money.
"""
user_proxy.initiate_chat(assistant, message=task_extra)

task1 = """
Find arxiv papers that show how are people studying trust calibration in AI based systems
"""
user_proxy.initiate_chat(assistant, message=task1)

task2 = "analyze the above the results to list the application domains studied by these papers "
user_proxy.initiate_chat(assistant, message=task2, clear_history=False)

task3 = """Use this data to generate a bar chart of domains and number of papers in that domain and save to a file
"""
user_proxy.initiate_chat(assistant, message=task3, clear_history=False)

task4 = """Reflect on the sequence and create a recipe containing all the steps
necessary and name for it. Suggest well-documented, generalized python function(s)
 to perform similar tasks for coding steps in future. Make sure coding steps and
 non-coding steps are never mixed in one function. In the docstr of the function(s),
 clarify what non-coding steps are needed to use the language skill of the assistant.
"""
user_proxy.initiate_chat(assistant, message=task4, clear_history=False)