class Register:
    def __init__(self, name):
        self.name = name
        self.contents = None

    def dispatch(self, message, value=None):
        match (message):
            case "get":
                return self.contents
            case "set":
                self.contents = value
            case _:
                raise ValueError(f"Unknown message: {message}")
