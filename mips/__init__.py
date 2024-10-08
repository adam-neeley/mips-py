from mips.machine import Machine


def main():
    code = """
    main:
        li   $s0 0
        li   $v0 4
    loop:
        la   $a0 $s0
        syscall
        addi $s0 $s0 1
        j    loop
    """
    machine = Machine()
    machine.assemble(code)
    machine.run()


if __name__ == "__main__":
    main()
