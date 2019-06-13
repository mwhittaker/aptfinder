import slack

from .settings import Settings

class SlackClient:
    def __init__(self,
                 token: str,
                 listings_channel: str,
                 debug_channel: str) -> None:
        self.listings_channel = listings_channel
        self.debug_channel = debug_channel
        self.slack_client = slack.WebClient(token)

    def post_listing(self, s: str) -> None:
        icon_url = ('https://upload.wikimedia.org/wikipedia/' +
                    'commons/thumb/f/f6/HAL9000.svg/400px-HAL9000.svg.png')
        self.slack_client.chat_postMessage(channel=self.listings_channel,
                                           text=s,
                                           as_user=False,
                                           username='Apartment Bot',
                                           icon_url=icon_url)

    def debug(self, s: str) -> None:
        print(s)

        icon_url = ('https://upload.wikimedia.org/wikipedia/' +
                    'commons/thumb/f/f6/HAL9000.svg/400px-HAL9000.svg.png')
        self.slack_client.chat_postMessage(channel=self.debug_channel,
                                           text=s,
                                           as_user=False,
                                           username='Apartment Bot',
                                           icon_url=icon_url)
