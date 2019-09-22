from bs4 import BeautifulSoup
from collections import namedtuple

def parse_coindesk(html):
    soup = BeautifulSoup(html, "html.parser")
    article_link_elements = []
    article_link_elements += soup.find_all("a", {"class": "stream-article"})
    article_link_elements += soup.find_all("a", {"class": "top-article"})
    article_link_elements += soup.find_all("a", {"class": "feature"})

    articles = []
    Article = namedtuple('Article', 'id source title link')

    index = 1
    for tag in article_link_elements:
        article_info = Article("coindesk-"+str(index), "coindesk", \
            tag["title"], tag["href"])
        articles.append(article_info)
        index += 1

    return articles

dispatcher = {"coindesk": parse_coindesk}



