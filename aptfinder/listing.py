from datetime import datetime
from typing import NamedTuple, Optional

class Listing(NamedTuple):
    website: str
    id: str
    url: str
    name: str
    price: int
    distance_to_soda: Optional[float]
    date_posted: Optional[datetime]

    def to_slack_string(self) -> str:
        if self.distance_to_soda is not None:
            distancestr = f'{self.distance_to_soda:.2f}'
        else:
            distancestr = 'UNKNOWN'

        if self.date_posted is not None:
            datestr = self.date_posted.strftime("%A, %B %d @ %H:%M")
        else:
            datestr = 'UNKNOWN'

        return (f'`[{self.id} @ {self.website}]` *${self.price}* | ' +
                f'*{distancestr} miles* from Soda | ' +
                f'posted {datestr} | ' +
                f'<{self.url}|details>')
