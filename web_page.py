from urllib.error import URLError
from urllib.request import Request, urlopen

from logger import Logger


class Webpage:
    """Webpage object."""

    def __init__(self, url: str):
        self.log = Logger.custom_logger(__file__)
        self.segmented_url: list = self.segment_url(url)
        if self.is_https_url(url):
            self.base_url: str = url
            self.body: bytes = self.retrieve_page(url)
            self.log.debug(f'{self.segmented_url=}')

    def retrieve_page(self, url):
        """Download full web page for requested URL."""
        try:
            request = Request(
                url, headers={'User-Agent': 'Mozilla/5.0'})
            page = urlopen(request).read()
            self.log.info(f"Retrieved requested webpage at {url}")
            return page
        except URLError as url_err:
            raise type(url_err)(
                f"Failed to retrieve the request webpage at {url}")

############################ REPLACE WITH urllib.parse ###########################################

    def segment_url(self, url):
        """Splits the URL on forward slashes."""
        url_segmented = url.split('/')
        return url_segmented

    def join_url(self, segmented_url):
        """Reconstructs the segmented URL with forward slashes."""
        return '/'.join(segmented_url)

    def is_https_url(self, url: str):
        """Checks if URL conforms to secure https."""
        prefix: list = self.segment_url(url)[0]
        is_https = False
        if 'https:' == prefix:
            self.log.info(f"Established secure connection to {url}")
            is_https = True
        elif 'http:' == prefix:
            self.log.warning(
                f"{url} http is not secure; did not attempt connection. Prefix URL with https://")
        else:
            self.log.warning(f"{url} is not HTTP. Prefix URL with https://")
        return is_https

###################################################################################################
