from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

chain.invoke({"topic": "your fat mom"})

## RAG - Retrieval augmented generation
# pip install langchain docarray
# Requires:
# pip install langchain docarray tiktoken pydantic==1.10.9 (new pydantic not compatible with docarray)

from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.embeddings import GPT4AllEmbeddings
from dotenv import load_dotenv

load_dotenv()
# from gpt4all import Embed4All
# text = 'The quick brown fox jumps over the lazy dog'
# embedder = Embed4All()
# output = embedder.embed(text)
# print(output)

## in memory vectorstore
vectorstore = DocArrayInMemorySearch.from_texts(
    ["harrison worked at kensho", "bears like to eat honey"],
    # embedding=OpenAIEmbeddings(),
    embedding=GPT4AllEmbeddings(),
    # eddings(),
)
retriever = vectorstore.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
model = ChatOpenAI()  # no gpt4all chat model available?
output_parser = StrOutputParser()

setup_and_retrieval = RunnableParallel(
    {"context": retriever, "question": RunnablePassthrough()}
)
chain = setup_and_retrieval | prompt | model | output_parser

chain.invoke("where did harrison work?")



retriever.invoke("where did harrison work?")


