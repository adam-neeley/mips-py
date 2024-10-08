from enum import Enum
from mips.console import console
import mips.operations as operations
from dataclasses import dataclass
from abc import ABC
from typing import Callable
import re


class Operation:
    def __init__(self, name, arg_format=""):
        self.name = name
        self.arg_format = arg_format

    def load_args(self, *args):
        expect_num_args = arg_format.split(", ")
        num_args = len(args)
        if num_args != expect_num_args:
            raise ValueError("Expected {expect_num_args} args but got {num_args}")
        return args

    def perform(self, machine, *args):
        self.load_args(*args)

    @staticmethod
    def create(name, arg_format):
        """
        R: arg_format = "$rd, $rs, $rt"
        I: arg_format = "$rt, $rs, IMM"
        J: arg_format = "PSEUDO_ADDRESS"
        """
        return Operation(name, arg_format)


class Procedure:
    """
    A class to represent a procedure.
    """

    @classmethod
    def All(cls):
        for subclass in cls.__subclasses__():
            yield from subclass.All()
            yield subclass

    def proc(self, machine):
        print("Not implemented")

    @property
    def type(self):
        return type(self).__name__

    def __repr__(self):
        return self.type


@dataclass
class Label(Procedure):
    Pattern = r"\w+(?=:)"
    name: str
    line: int

    def __init__(self, name, line):
        print("LABEL: ", name, line)
        self.name = name.strip()
        self.line = line

    def proc(self, machine):
        machine.set_value("$pc", self.line + 1)

    def __repr__(self):
        return f"""
        name:   {self.name}
        line:   {self.line}
        """


class Instruction(Procedure):
    Pattern = r"(\w|\s)+$"

    def __init__(self, expr):
        self.expr = expr
        self.tokens = self.tokenize(expr)
        if len(self.tokens) == 0:
            raise ValueError(f"Invalid Instruction expr: {expr}")
        self.op = self.tokens[0]
        if self.op not in operations.Locals:
            raise ValueError(f"Op not found: {self.op}")

    def tokenize(self, expr):
        res = []
        for token in expr.split(" "):
            if token == "":
                continue
            res.append(token.strip())
        return res

    def proc(self, machine):
        operations.run(machine, *self.tokens)
        print(machine)

    def __repr__(self):
        text = f"""
        expr:   {self.expr.strip()}
        tokens: {", ".join(self.tokens)}
        """
        res = ""
        for line in text.split("\n"):
            res += line.strip() + "\n"
        return res


class InstrType(Enum):
    Jump = 1
    Register = 2
    Immediate = 3


class Blank(Procedure):
    # Pattern = r"\s*"
    Pattern = r".*"

    def proc(self, machine):
        pass

    def __repr__(self):
        return ""
