from typing import Any, Dict, NamedTuple
import json

class Settings(NamedTuple):
    min_price: int
    max_price: int
    sleep_interval: int
    listings_channel: str
    debug_channel: str
    slack_token: str
    database_file: str

def from_json(d: Dict[str, Any]) -> Settings:
    return Settings(
        min_price=d['min_price'],
        max_price=d['max_price'],
        sleep_interval=d['sleep_interval'],
        listings_channel=d['listings_channel'],
        debug_channel=d['debug_channel'],
        slack_token=d['slack_token'],
        database_file=d['database_file'])

def from_file(filename: str) -> Settings:
    with open(filename, 'r') as f:
        return from_json(json.load(f))
