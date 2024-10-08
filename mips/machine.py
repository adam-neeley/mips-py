import re
import time

from mips.stack import Stack
from mips.register import Register
from mips.procedure import *
from mips.console import console


class Machine:
    "Class to represent a machine."

    def __init__(self):
        self.init_stack()
        self.init_labels()
        self.init_registers()
        self.init_operators()
        self.init_procedures()

    """Stack"""

    def init_stack(self):
        self.stack = Stack()

    """Registers"""

    RegisterNames = [
        "zero",
        "pc",
        "flag",
        "a0",
        "a1",
        "v0",
        "v1",
        "s0",
        "sp",
    ]

    """Init"""

    def init_labels(self):
        self.__labels = []

    def init_registers(self):
        self.__registers = []
        for name in Machine.RegisterNames:
            self.add_register(name)

    @property
    def labels(self):
        return self.__labels

    @property
    def registers(self):
        return self.__registers

    def add_label(self, label):
        self.__labels.append(label)

    def get_label(self, name):
        for i, l in enumerate(self.labels):
            if l.name == name:
                return self.labels[i]
        raise ValueError(f"Label not found: {name}")

    def add_register(self, register_name):
        self.__registers.append(Register(register_name))

    def get_value(self, name):
        if name[0] == "$":
            return int(self.get_register(name).contents)
        else:
            return int(self.get_label(name).line)

    def set_value(self, name, value):
        self.get_register(name).contents = value
        # return value

    def get_register(self, name):
        if name[0] == "$":
            name = name[1:]
        else:
            raise ValueError(f"Must start with $: {name}")

        for i, r in enumerate(self.registers):
            if r.name == name:
                return self.registers[i]
        raise ValueError(f"Register not found: {name}")

    """Operators"""

    def init_operators(self):
        self.operators = []

    """Procedures"""

    @property
    def procedures(self):
        return self.__procedures

    def init_procedures(self):
        self.__procedures = []

    def add_procedure(self, proc):
        proc.line = len(self.__procedures)
        self.__procedures.append(proc)

    """Assembler"""

    def assemble(self, controller_text):
        self.parse(controller_text)

    def parse(self, text):
        lines = text.strip().strip("\n").split("\n")
        line_number = 0
        while line_number < len(lines):
            line = lines[line_number]
            for Proc in Procedure.All():
                res = re.search(Proc.Pattern, line)
                if not res:
                    continue
                proc = Blank()
                match Proc.__name__:
                    case "Label":
                        proc = Label(name=res.group(), line=line_number)
                        self.add_label(proc)
                    case "Instruction":
                        proc = Instruction(
                            expr=line.strip()
                        )  # TODO add line=line_number
                line_number += 1
                self.add_procedure(proc)
                break

    """Running"""

    def start(self):
        while True:
            self.procedures[self.get_value("$pc")].proc(self)
            self.set_value("$pc", self.get_value("$pc") + 1)
            time.sleep(0.1)
        print("done")

    def __repr__(self):
        console.log("Machine")
        console.log("Labels")
        console.table([[i, l.name, l.line] for i, l in enumerate(self.labels)])
        console.log("Registers")
        console.table([[i, r.name, r.contents] for i, r in enumerate(self.registers)])
        console.log("Procedures")
        console.table([[l, p.type, p] for l, p in enumerate(self.procedures)])
        return ""
