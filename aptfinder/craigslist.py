from .geo import distance_to_soda
from .listing import Listing
from .scraper import Scraper
from .settings import Settings
from craigslist import CraigslistHousing
from datetime import datetime
from typing import Iterator, Optional

class CraigslistScraper(Scraper):
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def scrape(self) -> Iterator[Listing]:
        # TODO(mwhittaker): Don't hard code this.
        craigslist = CraigslistHousing(
            site='sfbay',
            category='apa',
            filters={
                'zip_code': 94720,
                'search_distance': 1,
                'min_price': self.settings.min_price,
                'max_price': self.settings.max_price,
            })

        kwargs = {'sort_by':'newest', 'geotagged':True, 'limit':20}
        for result in craigslist.get_results(**kwargs):
            # result['price'] looks something like '$1000'. To convert a price
            # to an integer, we remove the leading dollar sign.
            price = int(result['price'][1:])

            # Sometimes, result['geotag'] is None.
            distance: Optional[float] = None
            if result['geotag']:
                lat, lon = result['geotag']
                distance = distance_to_soda(lat, lon)

            # Parse date. Craigslist dates are of the form 2018-03-28 10:26.
            try:
                date_posted: Optional[datetime] = datetime.strptime(
                        result['datetime'], '%Y-%m-%d %H:%M')
            except Exception:
                date_posted = None

            yield Listing(
                    website='craigslist',
                    id=result['id'],
                    url=result['url'],
                    name=result['name'],
                    price=price,
                    distance_to_soda=distance,
                    date_posted=date_posted)
