import time
import argparse

from .settings import from_file
from .craigslist import CraigslistScraper

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('settings', help='JSON settings file.')
    args = parser.parse_args()
    settings = from_file(args.settings)

    scrapers = [
        CraigslistScraper(settings)
    ]

    # while True:
    for scraper in scrapers:
        for listing in scraper.scrape():
            print(listing)

if __name__ == '__main__':
    main()
