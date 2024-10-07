# class Execution:
# def __init__(self, inst):  # , labels, machine, pc, flag, stack, ops):


class Procedure:
    """
    A class to represent a procedure.
    """

    def __init__(self, machine, exec):
        self.__machine = machine
        self.__exec = exec

    @property
    def machine(self):
        return self.__machine

    @property
    def exec(self):
        return self.__exec


class Instruction:
    "A class to represent an instruction."

    def __init__(self, name, proc):
        "Initialize an instruction."
        self.name = name
        self.proc = proc
