from typing import Generator

from .listing import Listing

class Scraper:
    def scrape(self) -> Generator[Listing, None, None]:
        raise NotImplementedError()
