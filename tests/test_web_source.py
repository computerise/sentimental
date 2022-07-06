import unittest
from urllib.error import URLError

from sentimental import web_source

TEST_NAME = 'TEST_NAME'


class TestWebSource(unittest.TestCase):

    def test_web_source(self):
        self.source = web_source.WebSource(TEST_NAME)
        self.assertEqual(self.source.name, TEST_NAME)


if __name__ == '__main__':
    unittest.main()
