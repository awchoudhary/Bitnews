from bs4 import BeautifulSoup
from collections import namedtuple

def parse_coindesk(html):
    soup = BeautifulSoup(html, "html.parser")
    post_divs = soup.find_all("div", {"class": "post-info"})
    link_tags = []

    for div in post_divs:
        link_tags.extend(div.find_all("a", {"class": "fade"}))

    articles = []
    Article = namedtuple('Article', 'title link')

    for tag in link_tags:
        article_info = Article(tag.text.strip(), tag["href"])
        articles.append(article_info)

    return articles

dispatcher = {"coindesk": parse_coindesk}



