from mips.stack import Stack
from mips.register import Register


class Machine:
    def __init__(self, register_names=[], operations=[], controller_text=[]):
        self.__registers = {
            "pc": Register("pc"),
            "flag": Register("flag"),
        }

        self.__operations = []
        self.__controller = []

        for name in register_names:
            self.allocate_register(name)
        self.install_operations(operations)
        self.install_instruction_sequence(self.assemble(controller_text))

    def assemble(self, controller_text):
        raise NotImplementedError()

    def install_instruction_sequence(self, instruction_sequence):
        raise NotImplementedError()

    def install_operations(self, operations):
        raise NotImplementedError()

    def assemble(self, controller_text):
        raise NotImplementedError()

    @property
    def register(self, register_name):
        return self.__registers[register_name]

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

    def dispatch(self, message, value=None):
        match message:
            case "start":
                self.__registers["pc"].contents = 0
