import unittest
from urllib.error import URLError

import web_page

SECURE_URL = 'https://www.wsj.com/news/markets/stocks'
INSECURE_URL = 'http://www.google.com'
FAKE_URL = 'https:/wwafdfsdw.google.asdsdf'
NON_HTTP_URL = 'asdfaasf://wwafdfsdw.google.asdsdf'
SECURE_URL_SEGMENTED = ['https:', '',
                        'www.wsj.com', 'news', 'markets', 'stocks']


class TestWebpage(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestWebpage, self).__init__(*args, **kwargs)
        self.secure_url = web_page.Webpage(SECURE_URL)
        self.insecure_url = web_page.Webpage(INSECURE_URL)

    def test_is_https(self):
        self.assertEqual(
            self.secure_url.is_https_url(SECURE_URL), True)

    def test_segment_url(self):
        self.assertEqual(self.secure_url.segment_url(
            SECURE_URL), SECURE_URL_SEGMENTED)

    def test_join_url(self):
        self.assertEqual(self.secure_url.join_url(
            SECURE_URL_SEGMENTED), SECURE_URL)

    def test_insecure_url(self):
        self.assertFalse(
            self.insecure_url.is_https_url(INSECURE_URL))

    def test_non_http_url(self):
        self.assertFalse(
            self.insecure_url.is_https_url(NON_HTTP_URL))

    def test_fake_url(self):
        with self.assertRaises(Exception) as context:
            web_page.Webpage(FAKE_URL)
        self.assertTrue(
            'Failed to retrieve the request webpage at' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
