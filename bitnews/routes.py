from yattag import Doc
from flask import Flask
from flask import request
import articlescraper
import articlesearcher

app = Flask(__name__)

@app.route('/search')
def hello_world():
    query_string = request.args.get('querystring')
    all_articles = articlescraper.get_all_articles()
    found_articles = articlesearcher.get_articles_containing_words(all_articles, query_string.split())
    response = generate_html(found_articles)

    return response

        
def generate_html(articles):
    doc, tag, text = Doc().tagtext()
    html = []

    for article in articles:
        with tag("a", href = article.link):
            text(article.title + " - " + article.source)
        
        doc.stag('br')

    return doc.getvalue()