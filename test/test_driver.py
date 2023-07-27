"""Test drivers."""

import unittest

from sentimental.driver import SearchDriver

QUERY = "3M analyst ratings MarketWatch"


@unittest.skip
class TestDriver(unittest.TestCase):
    """Test Driver implementations."""

    def test_new_search(self) -> None:
        """Test new search with SearchDriver."""
        test_driver = SearchDriver()
        text = test_driver.google_text_search(QUERY)
        self.assertEqual(type(text), str)
