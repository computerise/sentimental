import unittest

from web_scraper import WebScraper
from driver import SearchDriver

SAMPLE_DATA = {'3M': {'High': 194.0, 'Median': 151.0,
                      'Low': 118.0, 'Average': 154.61}}


def remove_price(data):
    output_data = {}
    for company in data.values():
        try:
            company.pop('Price')
        except KeyError:
            print(KeyError)
        output_data.update(company)
    print(output_data)
    return output_data


class TestWebScraper(unittest.TestCase):

    def test_scrape(self):
        sample_data = remove_price(SAMPLE_DATA)
        scraper = WebScraper('S&P500', 's&p500.txt',
                             'MarketWatch', SearchDriver())
        data = remove_price(scraper.scrape_n(1, wait=0))
        self.maxDiff = 5000
        self.assertEqual(sample_data, data)


if __name__ == '__main__':
    unittest.main()
