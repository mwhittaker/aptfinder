from typing import Any, Dict, NamedTuple
import json

class Settings(NamedTuple):
    min_price: int
    max_price: int
    sleep_interval: int
    slack_channel: str
    slack_token: str
    database_file: str

def from_json(d: Dict[str, Any]) -> Settings:
    return Settings(d['min_price'], d['max_price'], d['sleep_interval'],
                    d['slack_channel'], d['slack_token'], d['database_file'])

def from_file(filename: str) -> Settings:
    with open(filename, 'r') as f:
        return from_json(json.load(f))
