import unittest

from driver import ChromeDriver, SearchDriver

QUERY = '3M analyst ratings MarketWatch'


class TestDriver(unittest.TestCase):

    def test_new_search(self):
        driver = SearchDriver()
        text = driver.google_text_search(QUERY)
        print(text)
        self.assertEqual(type(text), str)


if __name__ == '__main__':
    unittest.main()
