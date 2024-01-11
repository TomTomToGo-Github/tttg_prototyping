# https://medium.aiplanet.com/implement-rag-with-knowledge-graph-and-llama-index-6a3370e93cdd
## CHECK MTEP for best embedding models: https://huggingface.co/spaces/mteb/leaderboard
# pip install llama_index pyvis Ipython langchain pypdf

import logging
import sys
import os
from pathlib import Path
from dotenv import load_dotenv
from llama_index import (SimpleDirectoryReader,
                         LLMPredictor,
                         ServiceContext,
                         KnowledgeGraphIndex)
from llama_index.graph_stores import SimpleGraphStore
from llama_index.storage.storage_context import StorageContext
from llama_index.llms import HuggingFaceInferenceAPI
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from llama_index.embeddings import LangchainEmbedding
from pyvis.network import Network
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
path_documents = Path(r"C:\Users\thoma\Desktop\Tommy\Programmieren\tttg_prototyping\landchain\documents_rag")
llm = HuggingFaceInferenceAPI(
    model_name="HuggingFaceH4/zephyr-7b-beta", token=HF_TOKEN
)

embed_model = LangchainEmbedding(
  HuggingFaceInferenceAPIEmbeddings(api_key=HF_TOKEN,model_name="thenlper/gte-large")
)

documents = SimpleDirectoryReader(path_documents).load_data()
print(len(documents))

#setup the service context

service_context = ServiceContext.from_defaults(
    chunk_size=256,
    llm=llm,
    embed_model=embed_model
)

#setup the storage context

graph_store = SimpleGraphStore()
storage_context = StorageContext.from_defaults(graph_store=graph_store)

#Construct the Knowlege Graph Undex
index = KnowledgeGraphIndex.from_documents( documents=documents,
                                           max_triplets_per_chunk=3,
                                           service_context=service_context,
                                           storage_context=storage_context,
                                          include_embeddings=True)