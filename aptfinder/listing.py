from typing import NamedTuple, Optional
from datetime import datetime

class Listing(NamedTuple):
    website: str
    id: str
    url: str
    name: str
    price: int
    distance_to_soda: float
    date_posted: Optional[datetime]

    def to_slack_string(self) -> str:
        if self.date_posted is not None:
            datestr = self.date_posted.strftime("%A, %B %d @ %H:%M")
        else:
            datestr = 'UNKNOWN'
        return (f'`[{self.id} @ {self.website}]` *${self.price}* | ' +
                f'*{self.distance_to_soda:.2f} miles* from Soda | ' +
                f'posted {datestr} | ' +
                f'<{self.url}|details>')
