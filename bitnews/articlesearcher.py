word_to_articles_map = {}

def get_articles_containing_words(articles, words):
    found_articles = set()

    if(not word_to_articles_map):
        build_word_to_articles_map(articles)

    for word in words:
        if(word in word_to_articles_map):
            found_articles.update(word_to_articles_map[word])

    return found_articles

def build_word_to_articles_map(articles):
    for article in articles:
        words_in_title = article.title.split()
        
        for word in words_in_title:
            if(not word in word_to_articles_map):
                word_to_articles_map[word] = []

            word_to_articles_map[word].append(article)