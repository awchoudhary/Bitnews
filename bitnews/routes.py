from flask import Flask
import articlescraper

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = articlescraper.get_all_articles_links_in_html()
    return response