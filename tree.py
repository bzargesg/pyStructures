class Tree:
    def __init__(self, val):
        self.children = []
        self.val = val

    def add_child(self, val):
        newNode = Tree(val)
        self.children.append(newNode)
        return newNode

    def depth_print(self):
        result = []

        def recurse(node):
            # print('in recurse', node.val)
            if(len(node.children) == 0):
                result.append(node.val)
                return
            [recurse(nodeL) for nodeL in node.children]
            result.append(node.val)
        recurse(self)
        print(''.join(result))
