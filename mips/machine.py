from mips.stack import Stack
from mips.register import Register
from mips.instruction import Instruction


class Machine:
    def __init__(self, register_names=[], operations=[], controller_text=[]):
        self.__stack = Stack()

        self.__registers = {
            "pc": Register("pc"),
            "flag": Register("flag"),
        }

        self.__the_ops = {
            "initialize_stack": lambda: self.__stack,
        }

        self.__operations = []
        self.__controller = []
        self.__instructions = []

        for name in register_names:
            self.allocate_register(name)
        self.install_operations(operations)
        self.install_instruction_sequence(self.assemble(controller_text))

    def install_instruction_sequence(self, instruction_sequence):
        self.dispatch("install_instruction_sequence")(instruction_sequence)

    def install_operations(self, operations):
        self.dispatch("install_operations")(operations)

    def extract_labels(self, text, receive):
        pass
        if text == []:
            receive([], [])
        # result = text[]

    def assemble(self, controller_text):
        pass
        # result = self.extract_labels(controller_text, lambda insts, labels: self.up)
        # raise NotImplementedError()

    def lookup_register(self, register_name):
        if register_name in self.__registers.keys():
            return self.__registers[register_name]
        raise ValueError("Register not found: {register_name}")

    def execute(self):
        insts = pc.contents
        if insts == None:
            print("done")

    def allocate_register(self, name):
        for register_name in self.__registers.keys():
            if register_name == name:
                raise ValueError(f"Duplicate register: {name}")
        self.__registers[name] = Register(name)
        print("register allocated")

    def set_the_ops(self, ops):
        self.__the_ops = ops

    def set_the_instruction_seq(self, seq):
        self.__the_instruction_sequence = seq

    def update_insts(self, insts, labels):
        pc = self.lookup_register("pc")
        flag = self.lookup_register("flag")
        stack = self.__stack
        ops = self.__operations
        for inst in insts:
            self.set_instruction_execution_proc(
                inst,
                self.make_execution_procedure(inst.text, labels, pc, flag, stack, ops),
            )

    def dispatch(self, message, value=None):
        match message:
            case "start":
                self.__registers["pc"].contents = self.__the_instruction_sequence
                self.execute()
            case "install_instruction_sequence":
                return lambda seq: self.set_the_instruction_seq(seq)
            case "allocate_register":
                return self.allocate_register
            case "get_register":
                return self.lookup_register
            case "install_operations":
                return lambda ops: self.set_the_ops(self.__the_ops.update(ops))
            case "stack":
                return self.__stack
            case "ops":
                return self.__ops
            case _:
                raise ValueError(f"Unknown message: {message}")
