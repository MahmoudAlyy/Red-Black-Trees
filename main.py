from Tree import *
from Node import *
from tree_height import *
from Traversal import *
from DelMe import *

"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """
    #mandab's test input

    tree = RBTree()
    with open('English_Dictionary.txt','r') as fileobject:
        for line in fileobject:
            line="".join(line.split())
            tree.insert(line)
    #postorder(tree.root)
    if tree.search('a')==1:
        print('yes')
    else:
        print('no')
    tree.insert('newWord')
    tree.insert('newWord')

    #tree.printTree()       #dic is too long f mlhas lazma awi hna x)


    """
    #ngm's test input
    tree = RBTree()
    tree.insert(12)
    tree.insert(5)
    tree.insert(15)
    """
    tree.insert(3)
    tree.insert(10)
    tree.insert(13)
    tree.insert(17)
    tree.insert(4)
    tree.insert(7)
    tree.insert(11)
    tree.insert(14)
    tree.insert(6)
    tree.insert(8)
    """
    tree.printTree()      # el none el hwa el Nil w el $ dah eli hwa mfish y3ni

    print("#################################")

    test = tree.searchAndReturn(5)
    #inOrderSuccessor(test).printNode()
    DelMe(test)
    tree.printTree()
    #tree.root.left.printNode()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
