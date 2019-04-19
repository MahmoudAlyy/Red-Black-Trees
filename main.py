from Tree import *
from Node import *
from tree_height import *
from Traversal import *
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    tree = RBTree()
    with open('English_Dictionary.txt','r') as fileobject:
        for line in fileobject:
            tree.insert(line)
    postorder(tree.root)
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
