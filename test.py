import unittest
from hashTable import Hashtable
import hashTableHelpers


class Hash_table_test(unittest.TestCase):
    def setUp(self):
        Hashtable.testing = True

    def test_insert(self):
        print("Insert Tests:")
        hashT = Hashtable()
        hashT.insert('stuff', 7)
        index = hashTableHelpers.getIndexBelowMaxForKey('stuff', 8)
        arrVal = hashTableHelpers.LimitedArray(8)
        arrVal.set(index, [("stuff", 7)])
        self.assertListEqual(hashT.storage.storage,
                             arrVal.storage, "testing insert")

    # def retrieve_test(self):
    #     print("Retrieve Tests:")

    # def remove_test(self):
    #     print("Remove Tests:")


if __name__ == "__main__":
    unittest.main()
