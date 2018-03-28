from typing import List
import argparse
import time
import traceback

from .craigslist import CraigslistScraper
from .db import Database
from .padmapper import PadmapperScraper
from .settings import from_file
from .slack import SlackClient
from .listing import Listing

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('settings', help='JSON settings file.')
    args = parser.parse_args()
    settings = from_file(args.settings)

    db = Database(settings.database_file)
    slack_client = SlackClient(token=settings.slack_token,
                               listings_channel=settings.listings_channel,
                               debug_channel=settings.debug_channel)
    # TODO(mwhittaker): Debug and deploy PadmapperScraper.
    scrapers = [
        CraigslistScraper(settings),
        # PadmapperScraper(settings),
    ]


    try:
        while True:
            slack_client.debug(f'Scraping...')

            new_listings: List[Listing] = []
            for scraper in scrapers:
                for listing in scraper.scrape():
                    if not db.listing_exists(listing):
                        slack_client.post_listing(listing.to_slack_string())
                        new_listings.append(listing)
            db.insert_listings(new_listings)

            slack_client.debug(f'Found {len(new_listings)} new listings.')
            slack_client.debug(
                f'Sleeping for {settings.sleep_interval} seconds.')
            time.sleep(settings.sleep_interval)
    except Exception as e:
        slack_client.debug(traceback.format_exc())
        slack_client.debug(repr(e))

if __name__ == '__main__':
    main()
