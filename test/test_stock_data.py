"""Test stock data models."""

import unittest

from sentimental.stock_data import Company, CSVDataset

FILE_PATH = "data/sp500.csv"
STOCK_TICKER = "AAPL"
STOCK_NAME = "Apple"
STOCK_SECTOR = "Information Technology"


class TestDataset(unittest.TestCase):
    """Test Dataset."""

    def test_import_data(self) -> None:
        """Test importing data from CSV"""
        with open(FILE_PATH) as csv_file:
            self.dataset = CSVDataset(Company, csv_file)
        self.assertEqual(self.dataset.AAPL.ticker, STOCK_TICKER)
        self.assertEqual(self.dataset.AAPL.name, STOCK_NAME)
        self.assertEqual(self.dataset.AAPL.sector, STOCK_SECTOR)
