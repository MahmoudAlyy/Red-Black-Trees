from Node import *
from FixMe import *
class RBTree:
    """ red black tree """
    def __init__(self, root=None):
        self.root = root
        self.size = 0
    
    def search(self,key):
        if self.root == None:
            return -1
        current=self.root
        while(current != Nil):
            if key == current.value:
                return 1
            if key > current.value:
                current=current.right
            else:
                current=current.left
        return -1

    def insert(self , value):
        if self.search(value) ==1 :
            print("ERROR: Word already in the dictionary!")
            return
        node = Node(value)
        self.size+=1
        #if tree empty
        if self.root == None:
            self.root = node
            self.root.red = False
            print(self.getSize())
            print(tree_height(self.root))
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
        print(tree_height(self.root))
        print(self.getSize())
        return
    
    def getSize(self):
        return self.size