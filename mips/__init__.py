from mips.mips import MIPS


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

    MIPS.load(code)
    MIPS.assemble()
    MIPS.run()


if __name__ == "__main__":
    main()
