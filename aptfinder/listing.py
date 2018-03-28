from typing import NamedTuple
from datetime import datetime

class Listing(NamedTuple):
    website: str
    id: str
    url: str
    name: str
    price: int
    distance_to_soda: float
    date_posted: datetime

    def to_slack_string(self) -> str:
        return (f'`[{self.id} @ {self.website}]` *${self.price}* | ' +
                f'*{self.distance_to_soda:.2f} miles* from Soda | ' +
                f'posted {self.date_posted.strftime("%A, %B %d @ %H:%M")} | ' +
                f'<{self.url}|details>')
