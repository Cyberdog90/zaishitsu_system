import nfc

from zaishitsu import error
from zaishitsu.slack import Slack
from zaishitsu.plugin import Plugin
from zaishitsu.option import args


class Main:
    def __init__(self):
        slack = Slack()

        slack.set_url(url="<Your Token>")  # 本番
        plugin = Plugin()
        arguments = args()
        for name, instance in plugin.plugin_dict.items():
            if name in arguments:
                if eval(f"arguments.{name}"):
                    instance.set_active()
        self.last_id = None

        clf = nfc.ContactlessFrontend('usb')
        while True:
            clf.connect(rdwr={"on-connect": self.callback})

            for instance in plugin.plugins:
                if self.last_id == instance.nfc_id:
                    try:
                        instance.behavior()
                        self.last_id = None
                    except Exception as e:
                        error(str(e))

    def callback(self, tag):
        self.last_id = int.from_bytes(tag.identifier, "big")
        return True


if __name__ == "__main__":
    Main()
