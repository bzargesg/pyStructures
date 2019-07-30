import ctypes


class LimitedArray:
    storage = []
    limit = 0

    def __init__(self, limit):
        self.storage

    def get(self, index):
        self.checkLimit(index)
        return self.storage[index]

    def checkLimit(self, index):
        if(not isinstance(index, int) or self.limit <= index):
            raise IndexError

    def set(self, index, value):
        self.checkLimit(index)
        self.storage[index] = value

    def each(self, callback):
        for item in self.storage:
            callback(item, self.storage)


def getIndexBelowMaxForKey(str, max):
    hashval = 0
    for char in str:
        hashval = ctypes.c_int(hashval << 5 ^ 0).value + hashval + ord(char)
        hashval = hashval & hashval
        hashval = abs(hashval)
    return hashval % max
