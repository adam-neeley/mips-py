import re

from mips.stack import Stack
from mips.register import Register
from mips.instruction import Instruction


class Machine:
    "Class to represent a machine."

    def __init__(self, controller_text=""):
        self.init_stack()
        self.init_registers()
        self.init_operations()
        self.controller_text = controller_text

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

    def init_registers(self):
        self.registers = {}
        for name in Machine.RegisterNames:
            self.allocate_register(name)

    def allocate_register(self, register_name):
        self.register[register_name] = Register(register_name)

    """Operators"""

    def init_operators(self):
        self.operators = []

    """Instructions"""

    def install_operations(self, operations):
        self.dispatch("install_operations")(operations)

    """Labels"""

    def init_labels(self):
        self.labels = {"first": 0}

    def add_label(self, label, line):
        self.labels[label] = line

    def get_label(self, label):
        return self.labels[label]

    """Assembler"""

    def assemble(self):
        pass

    def parse(self, text):
        lines = text.split("\n")
        pats = [("label", r"^(\d+):")]
        for line, line_number in enumerate(lines):
            for type, pat in pats:
                res = re.match(pat, line)
                if res == None:
                    continue
                match type:
                    case "label":
                        self.add_label(res, line_number)
        print(self.labels)

    """Running"""

    def start(self):
        self.registers["pc"].contents = self.instruction_sequence
        self.execute()

    def execute(self):
        instructions = self.registers["pc"].contents
        if instructions == None:
            print("done")

    def install_instruction_sequence(self):
        self.registers["pc"].contents = self.instruction_sequence
        self.execute()
