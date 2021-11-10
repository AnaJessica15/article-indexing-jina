from flask import Flask, render_template, request
from search import indexing,search_results,prep_docs
from transformers import pipeline
import os
from newspaper import Article

app  = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')


@app.route("/summary", methods=["POST"])
def search():
    query = request.values.get("keyword")

    sum_len  = request.values.get("sum_len")

    data = search_results(flow, query)

    i = 0 

    for i in data:

        url = data[0].get('article_link')

    article = Article(url)

    article.download()

    article.parse()

    ARTICLE = article.text

    summarizer = pipeline("summarization")

    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    
    summary = summarizer(ARTICLE,max_length=130, min_length=int(sum_len), do_sample=False)

    return render_template('view.html', data = data,summary = summary)

    
if __name__ == "__main__":
    docs = prep_docs()
    flow = indexing(docs)
    app.run(debug = True,host="0.0.0.0")

