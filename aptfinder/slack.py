import slackclient

from .settings import Settings

class SlackClient:
    def __init__(self,
                 token: str,
                 listings_channel: str,
                 debug_channel: str) -> None:
        self.token = token
        self.listings_channel = listings_channel
        self.debug_channel = debug_channel
        self.slack_client = slackclient.SlackClient(token)

    def post_listing(self, s: str) -> None:
        self.slack_client.api_call('chat.postMessage',
                                   channel=self.listings_channel,
                                   text=s,
                                   user='Apartment Finder Bot')

    def debug(self, s: str) -> None:
        self.slack_client.api_call('chat.postMessage',
                                   channel=self.debug_channel,
                                   text=s,
                                   user='Apartment Finder Bot')
