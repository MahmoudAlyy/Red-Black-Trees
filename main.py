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
    tree.insert(50)
    tree.insert(20)
    tree.insert(70)
    tree.insert(65)
    tree.insert(75) 

    tree.insert(15)
    tree.insert(21)
    tree.insert(29)
    tree.insert(51)
    tree.insert(56)
    tree.insert(76)
    tree.insert(80)
 
    print("START**********************************")
    tree.printTree()      # el none el hwa el Nil w el $ dah eli hwa mfish y3ni

    print("END#################################")

    del_test = tree.searchAndReturn(29)
    DelMe(tree,del_test)

    tree.printTree()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
