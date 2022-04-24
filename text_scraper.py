from urllib.request import Request, urlopen

from logger import Logger

# Setup custom logger
log = Logger.custom_logger(__file__)


class Webpage:
    """Webpage object."""

    def __init__(self, url: str):
        if self.is_https_url(url) == True:
            self.base_url: str = url
            self.segmented_url: list = self.segment_url(url)
            self.body: bytes = self.retrieve_page(url)
            log.info(f'{self.segmented_url=}')

    def retrieve_page(self, url):
        """Download full web page for requested URL."""
        try:
            request = Request(
                url, headers={'User-Agent': 'Mozilla/5.0'})
            page = urlopen(request).read()
            log.info("Retrieved request web page")
            return page
        except Exception as ex:
            raise ConnectionError(f"{ex}: Failed to retrieve requested webpage.")


    def segment_url(self, url):
        """Splits the URL on forward slashes."""
        url_segmented = url.split('/')
        return url_segmented

    def is_https_url(self, url: str):
        """Checks if URL conforms to secure https."""
        if url[0:6] != 'https:':
            log.warning(f"{url} is not secure; did not attempt connection.")
            return False
        return True


class Source:
    """Source website object."""

    def __init__(self, url: str):
        """Initialise Source."""
        self.webpage: Webpage = Webpage(url)