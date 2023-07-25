import unittest

import sentimental.stock_data as stock_data

EXCHANGE_NAME = "sp500"
STOCK_TICKER = "AAPL"
STOCK_NAME = "Apple"
STOCK_SECTOR = "Information Technology"


class TestExchange(unittest.TestCase):
    def setUp(self, exchange=EXCHANGE_NAME, ticker=STOCK_TICKER, name=STOCK_NAME, sector=STOCK_SECTOR):
        self.dataset = stock_data.Exchange(exchange)
        self.ticker, self.name, self.sector = ticker, name, sector
        self.company = self.dataset.entries.get(ticker)

    def test_import_data(self):
        self.assertEqual(self.company.ticker, self.ticker)
        self.assertEqual(self.company.name, self.name)
        self.assertEqual(self.company.sector, self.sector)


if __name__ == "__main__":
    unittest.main()
