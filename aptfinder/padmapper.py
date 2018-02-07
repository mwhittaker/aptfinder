from typing import Generator

from .listing import Listing
from .scraper import Scraper
from .settings import Settings

class PadmapperScraper(Scraper):
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def scrape(self) -> Generator[Listing, None, None]:
        raise NotImplementedError()
