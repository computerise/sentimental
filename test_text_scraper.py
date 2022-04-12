import unittest

import text_scraper


class TestSource(unittest.TestCase):

    def test_retrieve_page(self):
        source = text_scraper.Source('https://www.google.com')
        self.assertEqual(type(source.webpage.body), bytes)
