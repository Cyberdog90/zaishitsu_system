from os import listdir
from typing import List
from copy import deepcopy
from importlib import import_module

from zaishitsu.abc_plugin import ABCPlugin
from zaishitsu import error

__all__ = ["Plugin"]


class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Plugin(Singleton):
    def __init__(self) -> None:
        self.__plugin_list: List[ABCPlugin] = []
        self.__plugin_dict: dict = dict()
        plugin_path = "./plugin"
        plugin_list = {plugin for plugin in listdir(plugin_path) if plugin[0] != "."}
        for plugin in plugin_list:
            try:
                self.__load_plugin(plugin)
            except Exception as e:
                error(str(e))

    def __load_plugin(self, plugin_name: str) -> ABCPlugin:
        package_plugin = import_module(name=f"plugin.{plugin_name}")
        instance = package_plugin.Plugin()
        self.__plugin_dict[plugin_name] = instance
        self.__plugin_list.append(instance)

    @property
    def plugins(self) -> List[ABCPlugin]:
        return self.__plugin_list

    @property
    def plugin_dict(self):
        return self.__plugin_dict
