# liberte_ai.py

import os
from django.conf import settings  # Make sure you have this imported
from langchain.chains import ConversationalRetrievalChain
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain_chroma import Chroma

from . import constants

os.environ["OPENAI_API_KEY"] = constants.APIKEY

# Determine the data directory path
DATA_DIR = os.path.join(settings.BASE_DIR, 'lbtchat', 'data')

# Debugging: Print the constructed DATA_DIR to verify
print(f"Data directory path: {DATA_DIR}")

# Ensure the data directory exists
if not os.path.isdir(DATA_DIR):
    raise FileNotFoundError(f"Data directory not found: {DATA_DIR}")

PERSIST = True
PERSIST_DIR = "persist"
LAST_INDEX_TIME_FILE = "last_index_time.txt"

embedding = OpenAIEmbeddings()
vectorstore_kwargs = {"persist_directory": PERSIST_DIR} if PERSIST else {}
index_creator = VectorstoreIndexCreator(vectorstore_cls=Chroma, vectorstore_kwargs=vectorstore_kwargs, embedding=embedding)

index = index_creator.from_loaders([DirectoryLoader(DATA_DIR), TextLoader(os.path.join(DATA_DIR, 'convo_training_data.txt'))])

chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-4"),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

def get_response_from_libertai(user_query):
    result = chain.invoke({"question": user_query, "chat_history": []})
    return result['answer']
