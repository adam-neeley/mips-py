class Register:
    "A class to represent a register."

    def __init__(self, name):
        "Initialize name and contents of register."
        self.__name = name
        self.__contents = None

    @property
    def name(self):
        return self.__name

    @property
    def contents(self):
        return self.__contents

    @contents.setter
    def contents(self, value):
        self.__contents = value
