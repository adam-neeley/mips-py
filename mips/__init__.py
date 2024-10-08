from mips.machine import Machine
from mips.register import Register
from mips.stack import Stack
from mips.procedure import *


def main():
    controller_text = """
    main:
        li   $s0 0
    loop:
        li   $v0 4
        la   $a0 $s0
        syscall
        addi $s0 $s0 1
        j    loop
    """
    machine = Machine()
    machine.assemble(controller_text)
    print(machine)
    machine.start()


if __name__ == "__main__":
    main()
