import sys
sys.path.append('./')
from bitnews import htmlparsers

import unittest


class HtmlParsersTests(unittest.TestCase):
    def test_parse_coindesk(self):
        #Arrange
        html = """
                <div class="main-feature">
                    <div class="article article-featured">
                        <a class="fade" href="https://www.coindesk.com/crypto-unicorn-bitmain-weighs-18-billion-ipo-one-of-worlds-largest/" title="Crypto Unicorn Bitmain Weighs $18 Billion IPO, One of World's Largest">
                            <div class="picture">
                                <img width="1500" height="1000" src="https://media.coindesk.com/uploads/2018/08/jihan-consensus-e1533904640187.jpg" class="attachment-full size-full wp-post-image" alt="" /> 
                            </div>
                            <div class="article-meta">
                                <h3 class="featured-article-title">Crypto Unicorn Bitmain Weighs $18 Billion IPO, One of World's Largest</h3>
                                <p class="timeauthor">
                                <time datetime="2018-08-10T17:00:48+00:00">Aug 10, 2018</time> by Ada Hui 
                                </p>
                            </div>
                        </a>
                    </div>
                </div>
                """
        link = "https://www.coindesk.com/crypto-unicorn-bitmain-weighs-18-billion-ipo-one-of-worlds-largest/"
        title = "Crypto Unicorn Bitmain Weighs $18 Billion IPO, One of World's Largest"
        
        #act
        articles = htmlparsers.parse_coindesk(html)

        #assert
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0].title, title)
        self.assertEqual(articles[0].link, link)


if __name__ == '__main__':
    unittest.main()
