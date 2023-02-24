import requests
import json

from zaishitsu.plugin import Plugin


class Slack:
    web_hook_url: str = "<Your Token>"


    @classmethod
    def set_url(cls, url: str):
        cls.web_hook_url = url

    @classmethod
    def post(cls, message: str):
        requests.post(cls.web_hook_url, data=json.dumps({
            "text": message,
        }))


if __name__ == '__main__':
    slack = Slack()
    slack.post("TEST")
