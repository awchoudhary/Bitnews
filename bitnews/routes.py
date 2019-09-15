from flask import Flask, request, render_template
import articlescraper
import articlesearcher

app = Flask(__name__)

@app.route('/')
def index():
    all_articles = articlescraper.get_all_articles()
    return render_template('index.html', articles = all_articles)

@app.route('/search')
def search():
    query_string = request.args.get('q')
    all_articles = articlescraper.get_all_articles()

    if query_string == '':
        return render_template('index.html', articles = all_articles)

    found_articles = articlesearcher.get_articles_containing_words(all_articles, query_string.split())

    return render_template('index.html', articles = found_articles)