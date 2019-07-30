class LinkedList:
    val = ''
    nextNode = None

    def __init__(self, value):
        self.val = value
        self.nextNode = None
# insert new node by value

    def insert(self, value):
        newNode = LinkedList(value)
        nodeIter = self
        while(nodeIter.nextNode):
            nodeIter = nodeIter.nextNode
        nodeIter.nextNode = newNode
