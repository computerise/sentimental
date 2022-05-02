import re
import time

from logger import Logger
from stock_data import CompanyDataset
from web_source import WebSource
from driver import ChromeDriver, SearchDriver

log = Logger.custom_logger(__file__, 'INFO')


class WebScraper:
    def __init__(self, company_dataset_name: str, company_dataset_file: str, source_name: str, driver=None):
        self.company_dataset = self.import_dataset(
            CompanyDataset, company_dataset_name, company_dataset_file)
        self.source = self.import_source(source_name)
        if driver is None:
            self.driver = ChromeDriver()
        else:
            self.driver = driver

    def import_dataset(self, dataset_type, name, file):
        return dataset_type(name, file)

    def import_source(self, name):
        return WebSource(name)

    def scrape_n(self, n: int, query='price target', wait=1):
        company_queries = list(self.company_dataset.companies.values())
        number_of_company_queries = len(company_queries)
        if n > number_of_company_queries:
            n = number_of_company_queries
        scraped_data = {}
        for company in company_queries[:n]:
            new_scrape = self.scrape(company.name, self.source.name, query)
            self.add_data(scraped_data, company.name, new_scrape)
            time.sleep(wait)
        return scraped_data

    def scrape(self, company_name, source_name, query):
        full_query = f'{company_name} {query} {source_name}'
        log.debug(f'Scraped results for "{full_query}"')
        return self.driver.google_text_search(full_query)

    def format_text_element(self, name: str, text_element: str, currency='$'):
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
                    return False
        return {name: formatted_text}

    def add_data(self, data: dict, name, new_entry):
        if new_entry:
            formatted_data = self.format_text_element(name, new_entry)
            if formatted_data:
                data.update(formatted_data)
                log.info(formatted_data)
        return data


if __name__ == '__main__':
    scraper = WebScraper('S&P500', 's&p500.txt', 'MarketWatch', SearchDriver())
    data = scraper.scrape_n(10, wait=0)
    log.info(data)
