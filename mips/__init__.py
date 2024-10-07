from mips.machine import Machine
from mips.register import Register
from mips.stack import Stack
from mips.procedure import *


def main():
    controller_text = """
    main:
        addi $a0 $zero 1
    second:
        jr $ra
    """
    machine = Machine()
    machine.assemble(controller_text)
    print(machine)


if __name__ == "__main__":
    main()
