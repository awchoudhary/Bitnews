import requests
import htmlparsers

url_map = {"coindesk": "https://www.coindesk.com/"}

def get_articles(key):
    url = url_map[key]
    page = requests.get(url).text
    parser = htmlparsers.dispatcher[key]

    articles = parser(page)

    return articles

    