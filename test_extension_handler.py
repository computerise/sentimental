import unittest

from extension_handler import ExtensionHandler


INPUT_PATH = '/this/is/an/example/file/path.txt'
INPUT_EXTENSION = 'test'
OUTPUT_PATH = '/this/is/an/example/file/path.test'


class TestFileHandler(unittest.TestCase):

    def test_change_file_extension(self):
        output_path = ExtensionHandler.change_file_extension(
            INPUT_PATH, INPUT_EXTENSION)
        self.assertEqual(output_path, OUTPUT_PATH)
