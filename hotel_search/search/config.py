import os

SCRAPERS = os.getenv('SCRAPERS', 'expedia,orbitz,priceline,travelocity,hilton').split(',')
SCRAPER_BASE_URL = os.getenv('SCRAPER_BASE_URL', 'http://localhost:9000/scrapers/')
