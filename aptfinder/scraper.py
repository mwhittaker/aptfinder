from .listing import Listing
from typing import Iterator

class Scraper:
    def scrape(self) -> Iterator[Listing]:
        raise NotImplementedError()
