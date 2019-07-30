import hashTableHelpers


class Hashtable:
    limit = 8
    storage = []
    size = 0

    def __init__(self, limit=8):
        self.storage = hashTableHelpers.LimitedArray(limit)
        self.limit = limit

    # inserts key value pair into hash table
    def insert(self, key, value):
        self.size = self.size+1
        index = hashTableHelpers.getIndexBelowMaxForKey(key, self.limit)
        position = self.storage.get(index)
        if(position):
            position.append(tuple((key, value)))
        else:
            self.storage.set(index, [tuple((key, value))])

    # returns value by key from hash table
    def retrieve(self, key):
        index = hashTableHelpers.getIndexBelowMaxForKey(key, self.limit)
        bucket = self.storage.get(index)
        return [value[1] for value in bucket if value[0] == key][0]

    # finds value by key and deletes from hash table
    def remove(self, key):
        self.size = self.size - 1
        index = hashTableHelpers.getIndexBelowMaxForKey(key, self.limit)
        bucket = self.storage.get(index)
        [value[1] for value in bucket if value[0] == key][0]
        for index in range(len(bucket)):
            if(bucket[index][0] == key):
                bucket.pop(index)
                break

    # TODO implement Resize
    # size > limit => double
    # size < .25 * limit => halve
    def resize(self):
        print(self.storage)

    # TODO check if resizing needs to occur

    def check_resize(self):
        print(self.storage)
