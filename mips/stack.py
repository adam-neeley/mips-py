class Stack:
    def __init__(self):
        self.__list = []

    def push(self, value):
        self.__list.append(value)

    def is_empty(self):
        return len(self.__list) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop empty stack")
        return self.__list.pop()

    @property
    def length(self):
        return len(self.__list)

    def top(self):
        return self.__list[self.length - 1]

    def bottom(self):
        return self.__list[0]
