import unittest

from extension_handler import ExtensionHandler


INPUT_PATH = '/this/is/an/example/file/path.txt'
INPUT_EXTENSION = 'test'
OUTPUT_PATH = '/this/is/an/example/file/path.test'
NO_EXTENSION_PATH = '/the/file/in/this/path/has/no/extension'


class TestFileHandler(unittest.TestCase):

    def test_change_file_extension(self):
        output_path = ExtensionHandler.change_file_extension(
            INPUT_PATH, INPUT_EXTENSION)
        self.assertEqual(output_path, OUTPUT_PATH)
    
    def test_remove_no_extension(self):  
        with self.assertRaises(ValueError) as context:
            ExtensionHandler.remove_file_extension(NO_EXTENSION_PATH)
        self.assertTrue('Specified file does not have a file extension' in str(context.exception))
            

if __name__ == '__main__':
   unittest.main()