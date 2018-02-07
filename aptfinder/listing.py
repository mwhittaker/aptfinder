from typing import NamedTuple
from datetime import datetime

class Listing(NamedTuple):
    website: str
    id: str
    url: str
    name: str
    price: int
    distance_to_soda: int
    date_posted: datetime
