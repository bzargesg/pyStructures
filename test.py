import unittest
from linkedList import LinkedList
from hashTable import Hashtable
from tree import Tree
import hashTableHelpers


class Tree_Test(unittest.TestCase):
    def setUp(self):
        Tree.testing = True

    def test_insert(self):
        a = Tree('a')
        b = a.add_child('b')
        c = a.add_child('c')
        d = b.add_child('d')
        e = b.add_child('e')
        f = c.add_child('f')
        g = c.add_child('g')
        self.assertIn(b, a.children)
        self.assertIn(c, a.children)
# class Linked_List_Test(unittest.TestCase):
#    def setUp(self):
#         LinkedList.testing = True

#     def test_LL_insert(self):
#         ll = LinkedList(5)
#         ll.insert(3)
#         ll.insert(1)
#         self.assertIs(ll.val, 5, 'Head value correct')
#         self.assertIs(ll.nextNode.val, 3, '2nd Node value correct')
#         self.assertIs(ll.nextNode.nextNode.val, 1, '3rd node value correct')

#     def test_LL_delete_head(self):
#         ll = LinkedList(5)
#         ll.insert(3)
#         ll.insert(1)
#         ll.delete(5)
#         self.assertIs(ll.val, 3, 'Head value correct after delete')

#     def test_LL_delete_mid(self):
#         ll = LinkedList(5)
#         ll.insert(3)
#         ll.insert(1)
#         ll.delete(3)
#         self.assertIs(ll.val, 5, 'Head correct after mid delete')
#         self.assertIs(ll.nextNode.val, 1, 'tail correct after mid delete')

#     def test_LL_delete_tail(self):
#         ll = LinkedList(5)
#         ll.insert(3)
#         ll.insert(1)
#         ll.delete(1)
#         self.assertIs(ll.val, 5, 'Head correct after mid delete')
#         self.assertIs(ll.nextNode.val, 3, 'tail correct after mid delete')
#         self.assertIs(ll.nextNode.nextNode, None,
#                       'tail correct after mid delete')

# class Hash_Table_Tests(unittest.TestCase):
#     def setUp(self):
#         Hashtable.testing = True

#     def test_insert(self):
#         hashT = Hashtable()
#         hashT.insert('stuff', 7)
#         index = hashTableHelpers.getIndexBelowMaxForKey('stuff', 8)
#         arrVal = hashTableHelpers.LimitedArray(8)
#         arrVal.set(index, [("stuff", 7)])
#         self.assertListEqual(hashT.storage.storage,
#                              arrVal.storage, "test single insertion")
#         hashT.insert('junk', 8)
#         index = hashTableHelpers.getIndexBelowMaxForKey('junk', 8)
#         arrVal.get(index).append(("junk", 8))
#         self.assertListEqual(hashT.storage.storage,
#                              arrVal.storage, "testing insert collision")

#     def test_retrieve(self):
#         hashT = Hashtable()
#         hashT.insert('stuff', 7)
#         hashT.insert('junk', 8)
#         hashT.insert('hiya', 9)
#         hashT.insert('doodly', 35)
#         self.assertIs(hashT.retrieve('hiya'), 9, 'retrieve Value')
#         self.assertIs(hashT.retrieve('junk'), 8, 'retrieve collision value')

#     def test_remove(self):
#         hashT = Hashtable()
#         hashT.insert('stuff', 7)
#         hashT.insert('junk', 8)
#         hashT.insert('hiya', 9)
#         hashT.insert('doodly', 35)
#         hashT.remove('stuff')
#         expectedVal = [[('junk', 8)], None, None, [
#             ('hiya', 9)], None, [('doodly', 35)], None, None]
#         self.assertListEqual(hashT.storage.storage,
#                              expectedVal, "Deleted stuff at index 1")


if __name__ == "__main__":
    unittest.main()
