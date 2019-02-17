class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, data):
        self.__stack.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop() was called on empty stack!")

        self.__stack = self.__stack[:-1]

    def top(self):
        if self.is_empty():
            raise IndexError("top() was called on empty stack!")

        return self.__stack[-1]

    def is_empty(self):
        return len(self.__stack) == 0
