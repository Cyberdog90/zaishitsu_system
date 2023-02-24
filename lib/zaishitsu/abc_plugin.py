from abc import ABCMeta, abstractmethod
from zaishitsu.args import Args

__all__ = ["ABCPlugin"]


class ABCPlugin(metaclass=ABCMeta):
    @abstractmethod
    def behavior(self):
        pass

    @abstractmethod
    def set_active(self):
        pass

    @property
    @abstractmethod
    def nfc_id(self) -> int:
        pass

    @property
    @abstractmethod
    def option_name(self) -> str:
        pass

    @property
    @abstractmethod
    def args(self) -> Args:
        pass
