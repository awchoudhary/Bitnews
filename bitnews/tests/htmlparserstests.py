import sys
sys.path.append('./')
from bitnews import htmlparsers

import unittest


class HtmlParsersTests(unittest.TestCase):
    def test_parse_coindesk(self):
        #Arrange
        html = """
                <div class="post-info">
                    <h3><a class="fade" href='https://www.coindesk.com/fincen-says-it-now-receives-1500-crypto-complaints-a-month/' title='FinCEN Says It Now Receives 1,500 Crypto Complaints a Month'>FinCEN Says It Now Receives 1,500 Crypto Complaints a Month</a></h3>
                    <p class="timeauthor"><time datetime="2018-08-10T19:10:42+00:00">Aug 10, 2018 at 19:10</time> | <cite>
                        <a href="https://www.coindesk.com/author/mshen/" title="Posts by Muyao Shen" class="author url fn" rel="author">Muyao Shen</a> </cite>
                    </p>
                    <p>FinCEN receives more than 1,500 reports every month from financial institutions regarding cryptocurrencies, a top official said Thursday.</p>
                </div>
                
                """
        link = "https://www.coindesk.com/fincen-says-it-now-receives-1500-crypto-complaints-a-month/"
        title = "FinCEN Says It Now Receives 1,500 Crypto Complaints a Month"
        
        #act
        articles = htmlparsers.parse_coindesk(html)

        #assert
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0].title, title)
        self.assertEqual(articles[0].link, link)

if __name__ == '__main__':
    unittest.main()
