import logging
import unittest
import datetime

from extension_handler import ExtensionHandler
import logger


INPUT_PATH = __file__
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '%(asctime)s:%(levelname)s:%(message)s:TESTLOG:'
LOG_PATH = __file__


class TestLogger(unittest.TestCase):

    def test_get_custom_logger(self):
        log = logger.Logger.custom_logger(
            INPUT_PATH, log_level=LOG_LEVEL, log_format=LOG_FORMAT)
        log.debug('TESTMESSAGE')
        with open(TestLogger.output_path()) as file:
            last_line = file.readlines()[-1].split(':')
            self.assertEqual(last_line[4], 'TESTMESSAGE')
            self.assertEqual(last_line[5], 'TESTLOG')
            self.assertEqual(last_line[6], '\n')

    def output_path():
        return ExtensionHandler.change_file_extension(INPUT_PATH, '.log')

if __name__ == '__main__':
   unittest.main()