import requests
import htmlparsers

url_map = {"coindesk": "https://www.coindesk.com/"}
_all_articles = []

def get_all_articles():
    global _all_articles

    if(not _all_articles):
        for site_name, url in url_map.items():
            _all_articles += scrape_articles(site_name, url)

    return _all_articles

def scrape_articles(key, url):
    page = requests.get(url).text
    parser = htmlparsers.dispatcher[key]

    articles = parser(page)

    return articles
    