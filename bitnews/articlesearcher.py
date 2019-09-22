import os
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir
import sys
import shutil

article_map = {}

def get_articles_containing_words(articles, words):
    found_articles = set()

    if(not article_map):
        create_corpus(articles)
        build_article_map(articles)

    ix = open_dir("indexdir")
    query = QueryParser("title", ix.schema).parse(words)
    with ix.searcher(weighting=scoring.Frequency) as searcher:
        results = searcher.search(query)
        for result in results:
            found_articles.update([article_map[result['id']]])
    
    return found_articles

def build_article_map(articles):
    for article in articles:
        article_map[article.id] = article

def create_corpus(articles):
    schema = Schema(title=TEXT,id=ID(stored=True),source=TEXT(stored=True))
    if os.path.exists("indexdir"):
        shutil.rmtree("indexdir")
    os.mkdir("indexdir")
    ix = create_in("indexdir", schema)
    writer = ix.writer()
    for article in articles:
        writer.add_document(title=article.title, id=article.id,\
          source=article.source)
    writer.commit()
