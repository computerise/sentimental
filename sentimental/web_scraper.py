import re
import time

from sentimental.logger import Logger
from sentimental.stock_data import CompanyDataset
from sentimental.web_source import WebSource
from sentimental.driver import ChromeDriver, SearchDriver

log = Logger.custom_logger(__file__, 'INFO')


class WebScraper:
    def __init__(self, dataset_name: str, dataset_file: str, source_name: str, driver=None):
        self.dataset = self.import_dataset(
            CompanyDataset, dataset_name, dataset_file)
        self.source = self.import_source(source_name)
        if driver is None:
            self.driver = ChromeDriver()
        else:
            self.driver = driver

    def import_dataset(self, dataset_type: CompanyDataset, name: str, file: str):
        """Return a dataset imported from the specified csv file."""
        return dataset_type(name, file)

    def import_source(self, name):
        """Return a Websource object."""
        return WebSource(name)

    def initialise_google(self, query='a'):
        self.driver.new_search(query)

    def scrape_n(self, n: int, query='price target', wait=1):
        """Scrape n number of results. If n is greater than the number of elements in the dataset"""
        # self.initialise_google()
        company_queries = list(self.dataset.entries.values())
        number_of_company_queries = len(company_queries)
        if n > number_of_company_queries:
            n = number_of_company_queries
        scraped_data = {}
        for company in company_queries[:n]:
            data_text = self.scrape(company.name, self.source.name, query)
            self.add_data(scraped_data, company.name, data_text)
            time.sleep(wait)
        return scraped_data

    def scrape(self, company_name, source_name, query):
        """Input query and return scraped text."""
        full_query = f'{company_name} {query} {source_name}'
        log.debug(f'Scraped results for "{full_query}"')
        return self.driver.google_text_search(full_query)

    def format_table_element(self, name: str, text_element: str, currency='$'):
        """Format the raw text element into a more usable data type."""
        formatted_text = {}
        text_list = re.split('\n| ', text_element)
        for i, string in enumerate(text_list):
            if currency in string:
                try:
                    formatted_text.update(
                        {text_list[i-1]: float(string.replace(currency, ''))})
                except ValueError as ex:
                    log.warning(
                        f'{type(ex).__name__}: Could not format text element')
                    formatted_text = string  # formatted string has no update method
        return {name: formatted_text}

    def add_data(self, data: dict, name: str, new_entry: str):
        """Add some new entry to an exisiting data dictionary."""
        if new_entry:
            formatted_data = self.format_table_element(name, new_entry)
            if formatted_data:
                data.update(formatted_data)
                log.info(formatted_data)
        return data


if __name__ == '__main__':
    scraper = WebScraper('S&P500', 'sentimental/s&p500.txt',
                         'MarketWatch', SearchDriver())
    data = scraper.scrape_n(10, wait=0)
    log.info(data)
