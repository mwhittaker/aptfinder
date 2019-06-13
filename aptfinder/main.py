from .craigslist import CraigslistScraper
from .db import Database
from .listing import Listing
from .padmapper import PadmapperScraper
from .settings import from_file
from .slack import SlackClient
from typing import List
import argparse
import time
import traceback

def main() -> None:
    # Read settings from the command line.
    parser = argparse.ArgumentParser()
    parser.add_argument('settings', help='JSON settings file.')
    args = parser.parse_args()
    settings = from_file(args.settings)

    # Set up database, slack client, and scrapers.
    db = Database(settings.database_file)
    slack = SlackClient(token=settings.slack_token,
                               listings_channel=settings.listings_channel,
                               debug_channel=settings.debug_channel)
    # TODO(mwhittaker): Debug and deploy PadmapperScraper.
    scrapers = [
        CraigslistScraper(settings),
        # PadmapperScraper(settings),
    ]

    # Scrape!
    try:
        while True:
            slack.debug('Scraping...')

            new_listings: List[Listing] = []
            for scraper in scrapers:
                for listing in scraper.scrape():
                    if not db.listing_exists(listing):
                        print(listing)
                        slack.post_listing(listing.to_slack_string())
                        new_listings.append(listing)
            db.insert_listings(new_listings)

            slack.debug(f'Found {len(new_listings)} new listings.')
            slack.debug(f'Sleeping for {settings.sleep_interval} seconds.')
            time.sleep(settings.sleep_interval)
    except Exception as e:
        strings = ['```', traceback.format_exc(), repr(e), '```']
        slack.debug('\n'.join(strings))

if __name__ == '__main__':
    main()
