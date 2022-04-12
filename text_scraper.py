import logging
from urllib.request import Request, urlopen


# Logging configuration
LOG_PATH = f'{__file__[:-3]}.log'
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = ('%(asctime)s:%(levelname)s:%(message)s')
logging.basicConfig(filename=LOG_PATH, level=LOG_LEVEL, format=LOG_FORMAT)


class Webpage:
    """Webpage object."""

    def __init__(self, url: str):
        self.base_url: str = url
        self.body = self.retrieve(url)

    def retrieve(self, url):
        """Download full web page for requested URL."""
        request = Request(
            url, headers={'User-Agent': 'Mozilla/5.0'})
        return urlopen(request).read()


class Source:
    """Source website object."""

    def __init__(self, url: str):
        """Initialise Source."""
        self.webpage: Webpage = Webpage(url)


source = Source('https://www.wsj.com/news/markets/stocks')
logging.debug(source.webpage.body)
