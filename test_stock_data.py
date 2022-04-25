import unittest

import stock_data

DATA_NAME = 's&p500'
DATA_PATH = 's&p500.txt'
STOCK_TICKER = 'AAPL'
STOCK_NAME = 'Apple'
STOCK_SECTOR = 'Information Technology'


class TestExchange(unittest.TestCase):

    def setup_test(self, data_name=DATA_NAME, path=DATA_PATH, ticker=STOCK_TICKER, name=STOCK_NAME, sector=STOCK_SECTOR):
        self.dataset = stock_data.Exchange(name, path)
        self.ticker, self.name, self.sector = ticker, name, sector
        self.company = self.dataset.companies.get(ticker)

    def test_import_stock_data(self):
        self.setup_test()
        self.assertEqual(self.company.ticker, self.ticker)
        self.assertEqual(self.company.name, self.name)
        self.assertEqual(self.company.sector, self.sector)

if __name__ == '__main__':
   unittest.main()