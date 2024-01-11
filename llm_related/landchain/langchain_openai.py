##built-in modules
import os
## pip installed modueles
from dotenv import load_dotenv
# from langchain.chat_models import ChatOpenAI, ChatPrxomptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain.schema.messages import SystemMessage, HumanMessage
from langchain.prompts import PromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.prompts.chat import ChatPromptTemplate
# Available: SystemMessage, ToolMessage, ChatMessage, HumanMessage, FunctionMessage, AIMessage
from langchain.chat_models import ChatOpenAI  ## chat_model.invoke() List of base messages -> output string
from langchain.llms import OpenAI  ## llm.invoke() Input string -> output string


## OpenAI
load_dotenv()
## Quick invoke
# Connect to llm and format messages
llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
chat_model = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
text = "What would be a good company name for a company that makes colorful socks?"
messages = [HumanMessage(content=text)]
# Invoke
answer_string_llm = llm.invoke(text)
answer_Message = chat_model.invoke(messages)  ## AIMessage
answer_string_chat = answer_Message.content


## More elaborate Chat model invoke with templates
template_translate = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"

## Two identical ways to format prompts
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template_translate),
    ("human", human_template),
])
prompt_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(template_translate),
    HumanMessagePromptTemplate.from_template(human_template),
])
formatted_prompt = prompt_template.format_prompt(input_language="English", output_language="French", text="I love programming.")
chat_model.invoke(formatted_prompt)

## Interesting way to combine template with messages
chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "You are a helpful assistant that re-writes the user's text to "
                "sound more upbeat."
            )
        ),
        HumanMessagePromptTemplate.from_template("Some form of text: {text}"),
    ]
)
