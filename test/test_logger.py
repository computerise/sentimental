"""Test logging."""

import logging
import unittest

from sentimental.extension_handler import ExtensionHandler
import sentimental.logger as logger


INPUT_PATH = __file__
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(asctime)s:%(levelname)s:%(message)s:TESTLOG:"
LOG_PATH = __file__


def output_path() -> str:
    """Change log output path."""
    return ExtensionHandler.change_file_extension(INPUT_PATH, ".log")


class TestLogger(unittest.TestCase):
    """Test Logger."""

    def test_get_custom_logger(self) -> None:
        """Test getting a custom logger."""
        log = logger.Logger.custom_logger(INPUT_PATH, log_level=LOG_LEVEL, log_format=LOG_FORMAT)
        log.debug("TESTMESSAGE")
        with open(output_path()) as file:
            last_line = file.readlines()[-1].split(":")
            self.assertEqual(last_line[4], "TESTMESSAGE")
            self.assertEqual(last_line[5], "TESTLOG")
            self.assertEqual(last_line[6], "\n")
