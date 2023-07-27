#!/usr/bin/env python3

"""Application entrypoint."""

from sentimental.web_scraper import GoogleScraper

if __name__ == "__main__":
    scraper = GoogleScraper("sp500", "MarketWatch")
    data = scraper.scrape_n(10, wait=0)
    print(data)
