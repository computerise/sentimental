import unittest

from web_scraper import WebScraper
from driver import SearchDriver

SAMPLE_DATA = {'3M': {'High': 210.0, 'Median': 161.0, 'Low': 118.0, 'Average': 163.67, 'Price': 144.21},
               'A. O. Smith': {'High': 96.0, 'Median': 80.0, 'Low': 59.0, 'Average': 80.22, 'Price': 63.34},
               'Abbott Laboratories': {'High': 154.0, 'Median': 141.0, 'Low': 115.0, 'Average': 141.21, 'Price': 116.72},
               'AbbVie': {'High': 192.0, 'Median': 167.5, 'Low': 115.0, 'Average': 165.07, 'Price': 157.62},
               'Accenture': {'High': 480.0, 'Median': 389.5, 'Low': 342.0, 'Average': 403.91, 'Price': 303.1},
               'Activision Blizzard': {'High': 100.0, 'Median': 95.0, 'Low': 82.0, 'Average': 94.09, 'Price': 76.1},
               'ADM': {'High': 111.0, 'Median': 99.0, 'Low': 68.0, 'Average': 95.67, 'Price': 93.92},
               'Adobe': {'High': 650.0, 'Median': 570.0, 'Low': 455.0, 'Average': 562.66, 'Price': 397.9},
               'Advance Auto Parts': {'High': 294.0, 'Median': 267.0, 'Low': 159.0, 'Average': 258.67, 'Price': 224.88}}


def remove_price(data):
    output_data = {}
    for company in data.values():
        company.pop('Price')
        output_data.update(company)
    return output_data


class TestWebScraper(unittest.TestCase):

    def test_scrape(self):
        sample_data = remove_price(SAMPLE_DATA)
        scraper = WebScraper('S&P500', 's&p500.txt',
                             'MarketWatch', SearchDriver())
        data = remove_price(scraper.scrape_n(10, wait=0))
        self.maxDiff = 5000
        self.assertEqual(sample_data, data)


if __name__ == '__main__':
    unittest.main()
