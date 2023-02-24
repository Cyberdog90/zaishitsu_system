class Args:
    def __init__(self, name: str, type, default) -> None:
        self.__name = name
        self.__type = type
        self.__default = default

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def default(self):
        return self.__default
