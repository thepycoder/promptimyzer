# 🎉 Promptimyzer 🎉

This is an example repo of how to use your own documentation to create a question answering bot using LangChain and the openAI API.

## Langchain

There is a langchain quickstart under `quickstart.ipynb`

## Documentation QA

You can ingest the documentation using `ingest.py` and then ask questions about it using `qa.py`

## Meta-optimizing

This is the subject of [this video](https://youtu.be/gR__vhOVvy4). You can see the elements at play one by one in `meta_optimizing.ipynb` or as a streamlit app in `meta_optimizing.py`. Run with stramlit:

```python
streamlit run meta_optimizing.py
```