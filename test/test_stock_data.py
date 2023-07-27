import unittest

from sentimental.stock_data import Company, CSVDataset

FILE_PATH = "data/sp500.csv"
STOCK_TICKER = "AAPL"
STOCK_NAME = "Apple"
STOCK_SECTOR = "Information Technology"


class TestDataset(unittest.TestCase):
    def setUp(self, path=FILE_PATH, ticker=STOCK_TICKER, name=STOCK_NAME, sector=STOCK_SECTOR):
        with open(path) as csv_file:
            self.dataset = CSVDataset(Company, csv_file)
        self.ticker, self.name, self.sector = ticker, name, sector
        self.company = self.dataset.AAPL

    def test_import_data(self):
        self.assertEqual(self.company.ticker, self.ticker)
        self.assertEqual(self.company.name, self.name)
        self.assertEqual(self.company.sector, self.sector)


if __name__ == "__main__":
    unittest.main()
