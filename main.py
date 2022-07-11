from sentimental import web_scraper as ws

scraper = ws.GoogleScraper('sp500', 'MarketWatch')
data = scraper.scrape_n(10, wait=0)
print(data)
