from zaishitsu.abc_plugin import ABCPlugin
from zaishitsu.slack import Slack
from zaishitsu.args import Args

__all__ = ["Plugin"]


class Plugin(ABCPlugin):
    def __init__(self):
        self.__nfc_id: int = 000000000000 # ID
        self.__option_name: str = "StdEL"
        self.__args = Args("StdEL", bool, False)

        self.__exist = False
        self.__enter_message = "鍵借りました"
        self.__leave_message = "鍵返しました"

    def behavior(self):
        if self.__exist:
            Slack.post(self.__leave_message)
        else:
            Slack.post(self.__enter_message)
        self.__exist = not self.__exist

    def set_active(self):
        self.__exist = True

    @property
    def nfc_id(self) -> int:
        return self.__nfc_id

    @property
    def option_name(self) -> str:
        return self.__option_name

    @property
    def args(self) -> Args:
        return self.__args
