from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    query = request.form['query']
    # Replace this with actual scraping logic
    result_text = f"You searched for: {query}"
    return render_template('result.html', result=result_text)

if __name__ == '__main__':
    app.run(debug=True)
