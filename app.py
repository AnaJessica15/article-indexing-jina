from flask import Flask, render_template, request
from search import indexing,search_results,prep_docs

app  = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')


@app.route("/summary", methods=["POST"])
def search():
    query = request.values.get("keyword")
    data = search_results(flow, query)
    return render_template('view.html', data = data)

    
if __name__ == "__main__":
    docs = prep_docs()
    flow = indexing(docs)
    app.run(debug = True,host="0.0.0.0")

