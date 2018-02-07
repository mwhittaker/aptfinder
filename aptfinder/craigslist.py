from typing import Generator

from craigslist import CraigslistHousing

from .geo import distance_to_soda
from .listing import Listing
from .scraper import Scraper
from .settings import Settings

class CraigslistScraper(Scraper):
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def scrape(self) -> Generator[Listing, None, None]:
        craigslist = CraigslistHousing(
            site='sfbay',
            category='apa',
            filters={
                'min_price': self.settings.min_price,
                'max_price': self.settings.max_price,
            })

        kwargs = {'sort_by':'newest', 'geotagged':True, 'limit':20}
        for result in craigslist.get_results(**kwargs):
            # result['price'] looks something like '$1000'. To convert a price
            # to an integer, we remove the leading dollar sign.
            price = int(result['price'][1:])

            # Sometimes, result['geotag'] is None.
            if result['geotag']:
                lat, lon = result['geotag']
                distance = distance_to_soda(lat, lon)
            else:
                distance = None

            yield Listing(
                    website='craigslist',
                    id=result['id'],
                    url=result['url'],
                    name=result['name'],
                    price=price,
                    distance_to_soda=distance,
                    date_posted=result['datetime'])
