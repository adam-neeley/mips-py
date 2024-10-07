class Stack:
    "A class to represent a stack."

    def __init__(self):
        "Initialize the stack."
        self.__list = []

    def push(self, value):
        "Add element to top of stack."
        self.__list.append(value)

    def is_empty(self):
        "Check if stack is empty."
        return len(self.__list) == 0

    def pop(self):
        "Remove and return top element."
        if self.is_empty():
            raise IndexError("Cannot pop empty stack")
        return self.__list.pop()

    @property
    def length(self):
        "Return number of elements in stack."
        return len(self.__list)

    def top(self):
        "Return top element of stack."
        return self.__list[self.length - 1]

    def bottom(self):
        "Return bottom element of stack."
        return self.__list[0]
