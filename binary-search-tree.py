class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if (self.root == None):
            self.root = Node (val)
        else:
            print ('inside add, root=', self.root.v)
            self._add (val, self.root)

    def _add(self, val, node):
        if (val < node.v):
            if (node.l != None):
                self._add (val, node.l)
            else:
                node.l = Node (val)
        else:
            if (node.r != None):
                self._add (val, node.r)
            else:
                node.r = Node (val)

    def find(self, val):
        if (self.root != None):
            print ('inside find, root=', self.root.v)
            return self._find (val, self.root)
        else:
            print ('inside not found, root=', self.root.v)
            return None

    def _find(self, val, node):
        if (val == node.v):
            return node
        elif (val < node.v and node.l != None):
            return self._find (val, node.l)
        elif (val > node.v and node.r != None):
            return self._find (val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self, order='in_order'):
        if (self.root != None):
            if (order == 'in_order'):
                self.in_order (self.root)
            elif (order == 'pre_order'):
                self.pre_order (self.root)
            elif (order == 'post_order'):
                self.post_order (self.root)

    def in_order(self, node):
        if (node != None):
            self.in_order (node.l)
            print (str (node.v) + ' ')
            self.in_order (node.r)

    def pre_order(self, node):
        if (node != None):
            print (str (node.v) + ' ')
            self.pre_order (node.l)
            self.pre_order (node.r)

    def post_order(self, node):
        if (node != None):
            self.post_order (node.l)
            self.post_order (node.r)
            print (str (node.v) + ' ')


# 3
# 0     4
#   2      8
tree = Tree ()

tree.add (3)
tree.add (4)
tree.add (0)
tree.add (8)
tree.add (2)
tree.printTree ()
tree.printTree ('post_order')
print (tree.getRoot ().v)
print ('finding 2:', end='')
print ((tree.find (2)))
print ('finding 10:', end='')
print (tree.find (10))
tree.deleteTree ()
tree.printTree ('post_order')
print ('bbye')
