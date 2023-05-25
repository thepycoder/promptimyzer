# 🎉 Promptimyzer 🎉

This is an example repo of how to use your own documentation to create a question answering bot using LangChain and the openAI API.

## Langchain

There is a langchain quickstart under `quickstart.ipynb`

## Documentation QA

You can ingest the documentation using `ingest.py` and then ask questions about it using `qa.py`

## Meta-optimizing

This is the subject of [this video](https://youtu.be/gR__vhOVvy4). You can see the elements at play one by one in `meta_optimizing.ipynb` or as a streamlit app in `meta_optimizing.py`. Run with streamlit:

```sh
# First, run ingest.py to generate the faiss_store.pkl and docs.index files
# based on the clearml-docs repo documentation
git clone https://github.com/allegroai/clearml-docs.git
python ingest.py

# Then run the app with streamlit
streamlit run meta_optimizing.py
```

## Setup

In addition to the Python packages in `requirements.txt`, you also need to download `en_core_web_sm` using the `spacy` package:

```sh
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
