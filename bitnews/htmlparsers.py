from bs4 import BeautifulSoup
from collections import namedtuple

def parse_coindesk(html):
    soup = BeautifulSoup(html, "html.parser")
    link_tags = soup.findAll("a", {"class": "fade"})
    articles = []
    Article = namedtuple('Article', 'title link')

    for tag in link_tags:
        article_info = Article(tag.text.strip(), tag["href"])
        articles.append(article_info)

    return articles

dispatcher = {"coin desk": parse_coindesk}



