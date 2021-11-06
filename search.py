
from jina import Flow, Executor, requests, Document, DocumentArray
import pandas as pd
import numpy as np
import os

def prep_docs():
    df = pd.read_csv('Article_dataset - Sheet1.csv')

    df = df.drop_duplicates().dropna()

    docs = DocumentArray()
    for i in range(df.shape[0]):
        heading = df.iloc[i, 0]
        link = df.iloc[i, -1]
        doc = Document(text = heading)
        doc.tags['article_link'] = link
        docs.append(doc)

    return docs
    

def indexing(docs):
    model = "sentence-transformers/paraphrase-distilroberta-base-v1"

    flow = (
        Flow()
        .add(
            name="error_text_encoder",
            uses="jinahub://TransformerTorchEncoder",
            uses_with={"pretrained_model_name_or_path": model},
            install_requirements = True
        )
        .add(
            name="error_text_indexer",
            uses='jinahub://SimpleIndexer',
            install_requirements = True
        )
    )

    os.system("rm -rf workspace")

    with flow:
        flow.index(
        inputs=docs,
            docs = docs,
            parameters = {'name' : 'somethign', 'xyz' : 'asdf'}
    )
    return flow


def search_results(flow, query):

    query = Document(text = input('Query product : '))
    with flow:
        response = flow.search(inputs = query, return_results = True)

    matches = response[0].docs[0].matches

    data = [
            {
                "article_heading :" :m.text,
                "article_link" : m.tags['article_link']
            } for m in matches[:5]
        ]

    return data