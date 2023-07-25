from sentimental import web_scraper

if __name__ == "__main__":
    scraper = web_scraper.GoogleScraper('sp500', 'MarketWatch')
    data = scraper.scrape_n(10, wait=0)
    print(data)
