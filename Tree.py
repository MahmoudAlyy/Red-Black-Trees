from Node import *
from FixMe import *
class RBTree:
    """ red black tree """
    def __init__(self, root=None):
        self.root = root

    def insert(self , value):
        node = Node(value)
        #node.printNode()
        #if tree empty
        if self.root == None:
            self.root = node
            self.root.red = False
            return
        #else
        currentNode = self.root
        while currentNode != None and currentNode != Nil :
            potentialParent = currentNode
            #node.printNode()
            #currentNode.printNode()
            if node.value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        node.parent = potentialParent
        if node.value < node.parent.value:
            node.parent.left = node
        else:
            node.parent.right = node
        fixme(self,node)
        #self.root.red = False
        return
