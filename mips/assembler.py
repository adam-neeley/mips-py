from mips.instruction import Instruction


def assemble(controller_text, machine):
    extract_labels(controller_text, lambda insts, labels: update_insts(insts, labels))


def update_insts(insts, labels, machine):
    pass


def extract_labels(text, receive):
    if text == None:
        self.__instructions = []
    else:
        self.extract_labels()
