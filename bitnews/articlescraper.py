import requests
import htmlparsers
from yattag import Doc

url_map = {"coindesk": "https://www.coindesk.com/"}
articles_map = {}

def get_all_articles():
    if(not articles_map):
        for site_name, url in url_map.items():
            articles = scrape_articles(site_name, url)
            articles_map[site_name] = articles

    response = generate_html(articles_map)

    return response

def scrape_articles(key, url):
    page = requests.get(url).text
    parser = htmlparsers.dispatcher[key]

    articles = parser(page)

    return articles
    
def generate_html(articles_with_source):
    doc, tag, text = Doc().tagtext()
    html = []

    for site_name, articles in articles_with_source.items():
        with tag("h2"):
            text(site_name)

        doc.stag('br')

        for article in articles:
            with tag("a", href = article.link):
                text(article.title)
            
            doc.stag('br')
            doc.stag('br')

    return doc.getvalue()
    