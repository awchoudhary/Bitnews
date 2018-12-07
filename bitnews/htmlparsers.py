from bs4 import BeautifulSoup
from collections import namedtuple

def parse_coindesk(html):
    soup = BeautifulSoup(html, "html.parser")
    article_link_elements = soup.find_all("a", {"class": "stream-article"})

    articles = []
    Article = namedtuple('Article', 'source title link')

    for tag in article_link_elements:
        article_info = Article("coindesk", tag["title"], tag["href"])
        articles.append(article_info)

    return articles

dispatcher = {"coindesk": parse_coindesk}



