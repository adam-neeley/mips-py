from mips.machine import Machine
from mips.register import Register
from mips.stack import Stack


def main():
    controller_text = """
    main:
        addi $a0, $zero, 1
    """
    machine = Machine(controller_text)
