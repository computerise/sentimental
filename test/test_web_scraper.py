import unittest

from sentimental.web_scraper import WebScraper
from sentimental.driver import SearchDriver

SAMPLE_DATA = {
    "Advance Auto Parts": {"High": 259.0, "Median": 220.0, "Low": 142.0, "Average": 222.21, "Price": 183.99},
    "Apple": {"High": 219.94, "Median": 185.0, "Low": 130.0, "Average": 184.79, "Price": 147.04},
    "AbbVie": {"High": 200.0, "Median": 160.0, "Low": 135.0, "Average": 163.81, "Price": 152.0},
}


def remove_price(data):
    output_data = {}
    for company in data.values():
        try:
            company.pop("Price")
        except KeyError:
            print(KeyError)
        output_data.update(company)
    print(output_data)
    return output_data


@unittest.skip
class TestWebScraper(unittest.TestCase):
    def test_scrape(self):
        sample_data = remove_price(SAMPLE_DATA)
        scraper = WebScraper("sp500", "MarketWatch", SearchDriver())
        data = remove_price(scraper.scrape_n(5, wait=0))
        self.maxDiff = 5000
        self.assertEqual(sample_data, data)
