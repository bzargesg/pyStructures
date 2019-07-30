import hashTableHelpers

# arr = hashTableHelpers.LimitedArray(10)
# val = hashTableHelpers.getIndexBelowMaxForKey('sstuff', 10)
# print(val)


class Hashtable:
    limit = 8
    storage = []
    size = 0

    def __init__(self, limit=8):
        self.storage = hashTableHelpers.LimitedArray(limit)
        self.limit = limit

    def insert(self, key, value):
        self.size = self.size+1
        index = hashTableHelpers.getIndexBelowMaxForKey(key, self.limit)
        position = self.storage.get(index)
        # print("position true?:", bool(position))
        if(position):
            position.append(tuple((key, value)))
        else:
            print("b4 insert", self.storage.print())
            self.storage.set(index, [tuple((key, value))])
            print("after insert", self.storage.print())

    def retrieve(self, key):
        print(self.storage)

    def remove(self, key):
        self.size = self.size - 1

    def resize(self):
        print(self.storage)

    def check_resize(self):
        print(self.storage)
