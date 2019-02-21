class HashTable:
    def __init__(self, size, array=[]):
        self.size = size
        self.length = 0
        self.hash_table = [[] for i in range(size)]
        # construct hash table through inserts
        for data in array:
            self.insert(data)

    def __len__(self):
        return self.length

    def insert(self, data):
        # get index
        index = self.hash(data)
        # insert
        self.hash_table[index].append(data)
        self.length += 1

    def hash(self, key):
        return key % self.size
