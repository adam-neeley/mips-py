from dataclasses import dataclass
import re


@dataclass
class Procedure:
    """
    A class to represent a procedure.
    """

    @classmethod
    def All(cls):
        for subclass in cls.__subclasses__():
            yield from subclass.All()
            yield subclass

    @property
    def type(self):
        return type(self).__name__

    def __repr__(self):
        return self.type


@dataclass
class Label(Procedure):
    Pattern = r"\w+(?=:)"
    name: str

    def __repr__(self):
        return self.name


@dataclass
class Instruction(Procedure):
    Pattern = r"\s*(\w|\s)+"
    expr: str

    def __repr__(self):
        return self.expr


@dataclass
class Blank(Procedure):
    Pattern = r".*"

    def __repr__(self):
        return ""
