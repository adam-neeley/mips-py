from mips.machine import Machine


def main():
    machine = Machine()
    machine.assemble(
        """
    main:
        li   $s0 0
    loop:
        li   $v0 4
        la   $a0 $s0
        syscall
        addi $s0 $s0 1
        j    loop
    """
    )
    machine.start()


if __name__ == "__main__":
    main()
