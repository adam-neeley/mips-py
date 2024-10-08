import re
import time

from mips.register import Register
from mips.procedure import Procedure, Blank, Label, Instruction
from mips.console import Console


class Machine:
    "Class to represent a machine."

    def __init__(self, registers, operators=[]):
        self.__labels = []
        self.__registers = []
        for name in registers:
            self.add_register(name)
        self.__procedures = []

    """Properties"""

    @property
    def labels(self):
        return self.__labels

    @property
    def registers(self):
        return self.__registers

    @property
    def procedures(self):
        return self.__procedures

    """Registers"""

    def add_register(self, register_name):
        self.__registers.append(Register(register_name))

    def get_register(self, name):
        if name[0] == "$":
            name = name[1:]
        else:
            raise ValueError(f"Must start with $: {name}")

        for i, r in enumerate(self.registers):
            if r.name == name:
                return self.registers[i]
        raise ValueError(f"Register not found: {name}")

    """Labels"""

    def add_label(self, label):
        self.__labels.append(label)

    def get_label(self, name):
        for i, l in enumerate(self.labels):
            if l.name == name:
                return self.labels[i]
        raise ValueError(f"Label not found: {name}")

    """Values"""

    def get_value(self, name):
        if name[0] == "$":
            return int(self.get_register(name).contents)
        else:
            return int(self.get_label(name).line)

    def set_value(self, name, value):
        if name[0] == "$":
            self.get_register(name).contents = value
        else:
            self.get_label(name).line = value

    """Procedures"""

    def add_procedure(self, proc):
        self.__procedures.append(proc)

    """Assembler"""

    def load(self, code):
        self.code = code

    def assemble(self):
        self.parse(self.code)

    def parse(self, text):
        lines = text.strip().strip("\n").split("\n")
        for line_num, line in enumerate(lines):
            for Proc in Procedure.All():
                res = re.search(Proc.Pattern, line)
                if not res:
                    continue
                proc = Blank()
                match Proc.__name__:
                    case "Label":
                        proc = Label(name=res.group(), line=line_num)
                        self.add_label(proc)
                    case "Instruction":
                        proc = Instruction(expr=line.strip())
                self.add_procedure(proc)
                break

    """Running"""

    def run(self):
        while True:
            self.procedures[self.get_value("$pc")].process(machine=self)
            self.set_value("$pc", self.get_value("$pc") + 1)
