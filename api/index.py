from flask import Flask, request
from duckduckgo_search import DDGS

app = Flask(__name__)

@app.route('/')
def hello_world():
    search_term = request.args.get('q')
    results = DDGS().text(search_term, max_results=5)
    return results

# if __name__ == '__main__':
#     app.run(debug=True, port=3000)
