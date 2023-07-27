"""Test logging."""

import logging
import unittest
from pathlib import Path

from sentimental.logger import Logger


INPUT_PATH = __file__
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(asctime)s:%(levelname)s:%(message)s:TESTLOG:"
LOG_PATH = Path(__file__).with_suffix(".log")


class TestLogger(unittest.TestCase):
    """Test Logger."""

    def test_get_custom_logger(self) -> None:
        """Test getting a custom logger."""
        log = Logger.custom_logger(INPUT_PATH, log_level=LOG_LEVEL, log_format=LOG_FORMAT, log_path=LOG_PATH)
        log.debug("TESTMESSAGE")
        with open(LOG_PATH) as file:
            last_line = file.readlines()[-1].split(":")
            self.assertEqual(last_line[4], "TESTMESSAGE")
            self.assertEqual(last_line[5], "TESTLOG")
            self.assertEqual(last_line[6], "\n")
