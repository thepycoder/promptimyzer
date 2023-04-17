"""Ask a question to the ClearML database."""
import os
# os.environ["LANGCHAIN_HANDLER"] = "langchain"

import faiss
from langchain import OpenAI
from langchain.chains import VectorDBQAWithSourcesChain
import pickle
import argparse

parser = argparse.ArgumentParser(description='Ask a question to the ClearML DB.')
parser.add_argument('question', type=str, help='The question to ask the ClearML DB')
args = parser.parse_args()

# Load the LangChain.
index = faiss.read_index("docs.index")

with open("faiss_store.pkl", "rb") as f:
    store = pickle.load(f)

store.index = index
chain = VectorDBQAWithSourcesChain.from_llm(llm=OpenAI(model_name="text-davinci-003", temperature=0.2), vectorstore=store)
result = chain({"question": args.question})
print(f"Answer: {result['answer']}")
print(f"Sources: {result['sources']}")