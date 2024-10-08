from mips.console import Console
import mips.operations as operations


class Procedure:
    """
    A class to represent a procedure.
    """

    @classmethod
    def All(cls):
        for subclass in cls.__subclasses__():
            yield from subclass.All()
            yield subclass

    def process(self, machine):
        raise NotImplementedError("Procedure process not implemented.")

    @property
    def type(self):
        return type(self).__name__

    def __repr__(self):
        return self.type


class Label(Procedure):
    Pattern = r"\w+(?=:)"

    def __init__(self, name, line):
        self.name = name.strip()
        self.line = line

    def process(self, machine):
        pass

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
        if self.op not in operations.Methods:
            raise ValueError(f"Op not found: {self.op}")

    def tokenize(self, expr):
        res = []
        for token in expr.split(" "):
            if token == "":
                continue
            res.append(token.strip())
        return res

    def process(self, machine):
        operations.run(machine, *self.tokens)

    def __repr__(self):
        text = f"tokens: {self.tokens}"
        res = ""
        for line in text.split("\n"):
            res += line.strip() + "\n"
        return res


class Blank(Procedure):
    Pattern = r"\s*"

    def process(self, machine):
        pass

    def __repr__(self):
        return ""
