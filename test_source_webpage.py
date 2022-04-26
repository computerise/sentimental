import unittest
from urllib.error import URLError

import source_webpage

SECURE_URL = 'https://www.wsj.com/news/markets/stocks'
INSECURE_URL = 'http://www.google.com'
FAKE_URL = 'https://wwafdfsdw.google.asdsdf'
NON_HTTP_URL = 'asdfaasf://wwafdfsdw.google.asdsdf'
SECURE_URL_SEGMENTED = ['https:', '', 'www.wsj.com', 'news', 'markets', 'stocks']


class TestSource(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSource, self).__init__(*args, **kwargs)
        self.secure_source = source_webpage.Source(SECURE_URL)
        self.insecure_source = source_webpage.Source(INSECURE_URL)

    def test_is_https(self):
        self.assertEqual(
            self.secure_source.webpage.is_https_url(SECURE_URL), True)

    def test_webpage_body(self):
        self.assertEqual(type(self.secure_source.webpage.body), bytes)

    def test_segment_url(self):
        self.assertEqual(self.secure_source.webpage.segment_url(
            SECURE_URL), SECURE_URL_SEGMENTED)
        
    def test_join_url(self):
        self.assertEqual(self.secure_source.webpage.join_url(SECURE_URL_SEGMENTED), SECURE_URL)

    def test_insecure_url(self):
        self.assertFalse(
            self.insecure_source.webpage.is_https_url(INSECURE_URL))

    def test_non_http_url(self):
        self.assertFalse(
            self.insecure_source.webpage.is_https_url(NON_HTTP_URL))

    def test_fake_url(self):
        with self.assertRaises(URLError) as context:
            source_webpage.Source(FAKE_URL)
        self.assertTrue('Failed to retrieve the request webpage at' in str(context.exception))
            
        
if __name__ == '__main__':
   unittest.main()
