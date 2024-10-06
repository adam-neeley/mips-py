from mips.machine import Machine
from mips.register import Register


def main():
    r = Register("name")
    r.dispatch("set", "value1")
    print(r.dispatch("get"))
