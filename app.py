from flask import Flask
from newsapi import NewsApiClient


app = Flask(__name__)

@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="661dbe8197a84484b4619c034ea00cb9")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")