from Tree import *
from Node import *
from tree_height import *
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    tree = RBTree()
    tree.insert(47)
    tree.insert(32)
    tree.insert(71)
    tree.insert(93)
    tree.insert(65)
    tree.insert(82)
    tree.insert(87)
    tree.root.printNode()
    tree.root.left.printNode()
    tree.root.right.printNode()
    tree.root.right.left.printNode()
    tree.root.right.right.printNode()
    tree.root.right.right.left.printNode()
    tree.root.right.right.right.printNode()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
