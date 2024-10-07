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


@dataclass
class Label(Procedure):
    Pattern = r"\w+(?=:)"
    name: str


@dataclass
class Instruction(Procedure):
    Pattern = r"\s*(\w|\s)+"
    expr: str


@dataclass
class Blank(Procedure):
    Pattern = r".*"
    pass
