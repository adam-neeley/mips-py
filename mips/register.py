class Register:
    def __init__(self, name):
        self.__name = name
        self.__contents = None

    def dispatch(self, message, value=None):
        print(f"{self.name} dispatch {message} {value}")
        match (message):
            case "get":
                return self.__contents
            case "set":
                self.__contents = value
            case _:
                raise ValueError(f"Unknown message: {message}")

    @property
    def name(self):
        return self.__name

    @property
    def contents(self):
        return self.dispatch("get")

    @contents.setter
    def contents(self, value):
        return self.dispatch("set", value)
