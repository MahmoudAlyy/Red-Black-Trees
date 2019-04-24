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

    tree = RBTree()
    while(1):
        s = input('================================\nPlease select a number that resmbles one of the following tasks:\n 1)Load Dictionary \n 2)Print Doctionary Size \n 3)Insert a word \n 4)Lookup a word \n 5)Delete a word\n Press any other key to Exit\n')
        if s == '1':
            filename = input('Please enter the filename:')
            with open(filename, 'r') as fileobject:
                for line in fileobject:
                    line = "".join(line.split())
                    tree.insert(line)
        elif s == '2':
            print(tree.getSize())
        elif s == '3':
            newWord = input("Please enter the word you wish to insert:")
            tree.insert(newWord)
            print("Size is")
            print(tree.getSize())
        elif s == '4':
            key = input('Please enter the word you wish to look-up:')
            if tree.search(key) == 1:
                print('Found')
            else:
                print('Not Found')
        elif s == '5':
            key = input('Please neter the word you wish to delete:')
            x = tree.searchAndReturn(key)
            DelMe(tree, x)
        else:
            break

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
