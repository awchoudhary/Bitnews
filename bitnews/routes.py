from flask import Flask
import articlescraper

app = Flask(__name__)

@app.route('/')
def hello_world():
    articles = articlescraper.get_articles("coindesk")
    returnString = ""
    titles = []

    for article in articles:
        titles.append(article.title)

    returnString = "<br><br>".join(titles)    

    return returnString