class Machine:
    def __init__(self, register_names, operations, controller_text):
        for name in register_names:
            self.allocate_register(name)
        self.install_operations(operations)
        self.install_instruction_sequence(self.assemble(controller_text))
