from datetime import datetime
from typing import Generator

import requests

from .geo import distance_to_soda
from .listing import Listing
from .scraper import Scraper
from .settings import Settings

class PadmapperScraper(Scraper):
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def scrape(self) -> Generator[Listing, None, None]:
        url = 'https://www.padmapper.com/api/t/1/pages/listables'
        data = {
            "built": ["newest"],
            "url": "berkeley-ca",
            "matching": True,
            "limit": 3,
            "offset": 20,
        }
        r = requests.post(url, json=data)

        if r.status_code == 434:
            assert r.json()['reason'] == 'missing xz_token'
            xz_token = r.json()['xz_token']
            headers = {'x-zumper-xz-token': xz_token}
            r = requests.post(url, json=data, headers=headers)

        for record in r.json()['listables']:
            # TODO(mwhittaker): Deal with min and max price.
            # TODO(mwhittaker): Deal with created and modified date.
            distance = distance_to_soda(record['lat'], record['lng'])
            yield Listing(
                    website='padmapper',
                    id=record['listing_id'],
                    url=f'https://padmapper.com{record["url"]}',
                    name=record['building_name'],
                    price=record['min_price'],
                    distance_to_soda=distance,
                    date_posted=datetime.fromtimestamp(record['modified_on']))

