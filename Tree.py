from Node import *
from FixMe import *
from tree_height import *
from collections import deque


class RBTree:
    """ red black tree """

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def search(self, key):
        if self.root == None:
            return -1
        current = self.root
        while(current != Nil):
            if key == current.value:
                return 1
            if key > current.value:
                current = current.right
            else:
                current = current.left
        return -1

    # same as the search above it but just retuns the node #might not be needed dk
    def searchAndReturn(self, key):
        if self.root == None:
            print('fuq')
            return Nil
        current = self.root
        while(current != Nil):
            if key == current.value:
                return current
            if key > current.value:
                current = current.right
            else:
                current = current.left
        return Nil

    def insert(self, value):
        if self.search(value) == 1:
            print("ERROR: Word already in the dictionary!")
            return
        node = Node(value)
        self.size += 1
        #if tree empty
        if self.root == None:
            self.root = node
            self.root.red = False
            return
        #else
        currentNode = self.root
        while currentNode != None and currentNode != Nil:
            potentialParent = currentNode
            if node.value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        node.parent = potentialParent
        if node.value < node.parent.value:
            node.parent.left = node
        else:
            node.parent.right = node
        fixme(self, node)
        print(self.getSize())
        return

    def getSize(self):
        return self.size

################### Copied just to help print tree for debugging #################################################
    def printTree(self):
        root = self.root
        buf = deque()
        output = []
        if not root:
            print('$')
        else:
            buf.append(root)
            count, nextCount = 1, 0
            while count:
                node = buf.popleft()
                if node:
                    string = ''
                    string = str(node.value)
                    if node.red == True:
                        string = string + ' R'
                    else:
                        string = string + ' B'
                    output.append(string)
                    count -= 1
                    for n in (node.left, node.right):
                        if n:
                            buf.append(n)
                            nextCount += 1
                        else:
                            buf.append(None)

                else:
                    output.append('$')
                if not count:
                    print(output)
                    output = []
                    count, nextCount = nextCount, 0
            # print the remaining all empty leaf node part
            output.extend(['$']*len(buf))
            print(output)
