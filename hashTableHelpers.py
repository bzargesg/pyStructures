import ctypes


class OutOfBoundsException(Exception):
    def __init__(self, ind, limit):
        message = f"index is out of bounds. Gave {ind} with bound {limit}"
        super().__init__(message)


class IndexIntException(Exception):
    def __init__(self):
        message = "Index is not an Int"
        super().__init__(message)


class LimitedArray:
    storage = []
    limit = 0

    def __init__(self, limit):
        self.storage = [None for num in range(limit)]
        self.limit = limit

    def get(self, index):
        self.checkLimit(index)
        return self.storage[index]

    def checkLimit(self, index):
        if(not isinstance(index, int)):
            raise IndexIntException()
        elif(self.limit <= index):
            raise OutOfBoundsException(index, self.limit)

    def set(self, index, value):
        self.checkLimit(index)
        self.storage[index] = value

    def each(self, callback):
        for item in self.storage:
            callback(item, self.storage)

    def print(self):
        return (self.storage)


def getIndexBelowMaxForKey(str, max):
    hashval = 0
    for char in str:
        hashval = ctypes.c_int(hashval << 5 ^ 0).value + hashval + ord(char)
        hashval = hashval & hashval
        hashval = abs(hashval)
    return hashval % max
