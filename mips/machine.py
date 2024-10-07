import re

from mips.stack import Stack
from mips.register import Register
from mips.procedure import *
from mips.console import console


class Machine:
    "Class to represent a machine."

    def __init__(self):
        self.init_stack()
        self.init_registers()
        self.init_operators()
        self.init_processes()

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
        "sp",
    ]

    @property
    def registers(self):
        return self.__registers

    def init_registers(self):
        self.__registers = []
        for name in Machine.RegisterNames:
            self.add_register(name)

    def add_register(self, register_name):
        self.__registers.append(Register(register_name))

    """Operators"""

    def init_operators(self):
        self.operators = []

    """Processes"""

    @property
    def processes(self):
        return self.__processes

    def init_processes(self):
        self.__processes = []

    def add_process(self, proc):
        proc.line = len(self.__processes)
        self.__processes.append(proc)

    def add_instruction(self, text):
        self.add_process(Instruction(expr=text.strip()))

    def add_label(self, text):
        self.add_process(Label(name=text))

    def add_blank(self):
        self.add_process(Blank())

    """Assembler"""

    def assemble(self, controller_text):
        self.parse(controller_text)

    def parse(self, text):
        lines = text.split("\n")
        line_number = 0
        while line_number < len(lines):
            line = lines[line_number]
            for Proc in Procedure.All():
                res = re.search(Proc.Pattern, line)
                if not res:
                    continue
                match Proc.__name__:
                    case "Label":
                        self.add_label(res.group())
                    case "Instruction":
                        self.add_instruction(res.group())
                    case _:
                        self.add_blank()
                line_number += 1
                break

    """Running"""

    def start(self):
        self.__registers["pc"].contents = self.instruction_sequence
        self.execute()

    def execute(self):
        instructions = self.__registers["pc"].contents
        if instructions == None:
            print("done")

    def install_instruction_sequence(self):
        self.__registers["pc"].contents = self.instruction_sequence
        self.execute()

    def __repr__(self):
        console.log("Machine")
        console.log("Registers")
        console.table([[i, r.name, r.contents] for i, r in enumerate(self.registers)])
        console.log("Procedures")
        console.table([[l, p.type, p] for l, p in enumerate(self.processes)])
        return ""
