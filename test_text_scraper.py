from aifc import Error
import unittest
from urllib.error import URLError

import text_scraper

SECURE_URL = 'https://www.wsj.com/news/markets/stocks'
INSECURE_URL = 'http://www.google.com'
FAKE_URL = 'https://wwafdfsdw.google.asdsdf'
SECURE_SOURCE = text_scraper.Source(SECURE_URL)
INSECURE_SOURCE = text_scraper.Source(INSECURE_URL)


class TestSource(unittest.TestCase):

    def test_is_https(self):
        self.assertEqual(
            SECURE_SOURCE.webpage.is_https_url(SECURE_URL), True)

    def test_webpage_body(self):
        self.assertEqual(type(SECURE_SOURCE.webpage.body), bytes)

    def test_segment_url(self):
        self.assertEqual(SECURE_SOURCE.webpage.segment_url(
            SECURE_URL), ['https:', '', 'www.wsj.com', 'news', 'markets', 'stocks'])

    def test_insecure_url(self):
        self.assertFalse(
            INSECURE_SOURCE.webpage.is_https_url(INSECURE_URL))

    def test_fake_url(self):
        with self.assertRaises(URLError) as context:
            text_scraper.Source(FAKE_URL)
        self.assertTrue('Failed to retrieve the request webpage at' in str(context.exception))
            
        
if __name__ == '__main__':
   unittest.main()
