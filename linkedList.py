class LinkedList:

    def __init__(self, value):
        self.val = value
        self.nextNode = None
        self.head = self

# insert new node by value
    def insert(self, value):
        newNode = LinkedList(value)
        nodeIter = self.head
        while(nodeIter.nextNode):
            nodeIter = nodeIter.nextNode
        nodeIter.nextNode = newNode

    def delete(self, value):
        nodeIter = self.head.nextNode
        prevNode = self.head
        if(self.val == value):
            self.head = self.nextNode
            self.val = self.nextNode.val
        else:
            while(nodeIter):
                if(nodeIter.val == value):
                    prevNode.nextNode = nodeIter.nextNode
                    print(nodeIter.nextNode)
                    break
                prevNode = nodeIter
                nodeIter = nodeIter.nextNode
