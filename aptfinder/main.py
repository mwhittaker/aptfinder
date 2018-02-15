import time
import argparse

from .craigslist import CraigslistScraper
from .db import Database
from .padmapper import PadmapperScraper
from .settings import from_file

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('settings', help='JSON settings file.')
    args = parser.parse_args()
    settings = from_file(args.settings)

    scrapers = [
        CraigslistScraper(settings),
        PadmapperScraper(settings),
    ]

    db = Database(settings.database_file)

    for scraper in scrapers:
        for listing in scraper.scrape():
            print(listing)
        db.insert_listings(scraper.scrape())

if __name__ == '__main__':
    main()
