## built-in modules
from pathlib import Path
## gpt4all
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.llms import GPT4All ## CALL IS DIFFERENT FROM STANDARD GPT4All
# from gpt4all import GPT4All as GPT4All2
from langchain.prompts import PromptTemplate

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

# Callbacks support token-wise streaming
callbacks = [StreamingStdOutCallbackHandler()]
model_name = "orca-2-7b.Q4_0.gguf"
model_path = Path(r"C:/Users/thoma/Desktop/Tommy/Programmieren/gpt4all/models")
llm = GPT4All(model=str(model_path / model_name))
llm_chain = LLMChain(prompt=prompt, llm=llm)
# Verbose is required to pass to the callback manager
# llm = GPT4All(model=str(model_path / model_name), callbacks=callbacks, verbose=True)
# If you want to use a custom model add the backend parameter
# Check https://docs.gpt4all.io/gpt4all_python.html for supported backends
# llm = GPT4All(model=str(model_path / model_name), backend="gptj", callbacks=callbacks, verbose=True)
question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"
llm_chain.run(question)
llm_chain.run(question=question)
