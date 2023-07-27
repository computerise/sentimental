"""Web scraper implementations."""

import re
import time

from sentimental.logger import Logger
from sentimental.driver import LinuxChromeDriver, SearchDriver

log = Logger.custom_logger(__file__, "INFO")


class WebScraper:
    """Webscraper class."""

    def __init__(self, source_name: str, driver: type[LinuxChromeDriver] = LinuxChromeDriver) -> None:
        """Initialise WebScraper."""
        self.source_name: str = source_name
        self.driver = type[LinuxChromeDriver] = driver()

    def scrape_n(self, n: int, query="price target", wait=1):
        """Scrape n number of results. If n is greater than the number of elements in the dataset"""
        company_queries = list(self.dataset.entries.values())
        number_of_company_queries = len(company_queries)
        if n > number_of_company_queries:
            n = number_of_company_queries
        scraped_data = {}
        for company in company_queries[:n]:
            data_text = self.scrape(company.name, self.source_name, query)
            self.add_data(scraped_data, company.name, data_text)
            time.sleep(wait)
        return scraped_data

    def scrape(self, company_name, source_name, query):
        """Input query and return scraped text."""
        full_query = f"{company_name} {query} {source_name}"
        log.debug(f'Scraped results for "{full_query}"')
        return self.driver.google_text_search(query=full_query)

    def format_table_element(self, name: str, text_element: str, currency="$"):
        """Format the raw text element into a more usable data type."""
        formatted_text = {}
        text_list = re.split("\n| ", text_element)
        for i, string in enumerate(text_list):
            if currency in string:
                try:
                    formatted_text.update({text_list[i - 1]: float(string.replace(currency, ""))})
                except ValueError as ex:
                    log.warning(f"{type(ex).__name__}: Could not format text element")
                    formatted_text = string  # formatted string has no update method
        return {name: formatted_text}

    def add_data(self, data: dict, name: str, new_entry: str):
        """Add some new entry to an existing data dictionary."""
        if new_entry:
            formatted_data = self.format_table_element(name, new_entry)
            if formatted_data:
                data.update(formatted_data)
                log.info(formatted_data)
        return data


class GoogleScraper(WebScraper):
    """WebScraper for Google search."""
    def __init__(self, data_name, source_name):
        """Initialise GoogleScraper."""
        super().__init__(data_name, source_name, driver=SearchDriver())
