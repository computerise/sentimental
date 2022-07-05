from driver import ChromeDriver, SearchDriver
import unittest
1

QUERY = '3M analyst ratings MarketWatch'


class TestDriver(unittest.TestCase):

    def test_new_search(self):
        driver = SearchDriver()
        text = driver.google_text_search(QUERY)
        self.assertEqual(type(text), str)


if __name__ == '__main__':
    unittest.main()
