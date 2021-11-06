'''
Created on : 10-10-2021

Created by : Ashwin Kumar, Ana Jessica, Ajay Kannan, Haris Murugan
    
'''

from flask import Flask,render_template,request
from summarizer import Summarizer,TransformerSummarizer
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

    model = TransformerSummarizer(transformer_type="XLNet",transformer_model_key="xlnet-base-cased")

    summary = ''.join(model(ARTICLE, min_length= int(sum_len)))

    return render_template('view.html',summary = summary)

if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0")

