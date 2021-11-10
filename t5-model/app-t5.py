'''
Created on : 10-10-2021

Created by : Ashwin Kumar, Ana Jessica

'''

from flask import Flask,render_template,request
from transformers import pipeline
import os
from newspaper import Article



app  = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def input():

    return render_template('index.html')


@app.route("/summary", methods=["GET","POST"])
def summary():


    url      = request.values.get("keyword")

    sum_len  = request.values.get("sum_len")

    # url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"    

    article = Article(url)

    article.download()

    article.parse()

    ARTICLE = article.text

    summarizer = pipeline("summarization")

    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    summary = summarizer(ARTICLE,max_length=130, min_length=int(sum_len), do_sample=False)

    return render_template('view.html',summary = summary)

if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0")

