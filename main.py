from sentimental import web_scraper as ws

scraper = ws.WebScraper('S&P500', 'sentimental/data/s&p500.txt',
                        'MarketWatch', ws.SearchDriver())
data = scraper.scrape_n(10, wait=0)
print(data)
