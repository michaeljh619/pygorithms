class Queue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, data):
        self.__queue.insert(0, data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue() was called on empty queue")

        data = self.__queue[0]
        self.__queue.pop(0)
        return data

    def is_empty(self):
        return len(self.__queue) == 0
