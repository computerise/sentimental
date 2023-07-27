import unittest

from sentimental.driver import SearchDriver

QUERY = "3M analyst ratings MarketWatch"


@unittest.skip
class TestDriver(unittest.TestCase):
    def test_new_search(self):
        test_driver = SearchDriver()
        text = test_driver.google_text_search(QUERY)
        self.assertEqual(type(text), str)
