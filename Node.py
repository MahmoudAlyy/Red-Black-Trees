from tree_height import *
class Node:
    """ red black tree node class """

    def __init__(self, value):
        self.value = value
        self.red = True # if false then black
        self.parent = None
        self.right = Nil
        self.left = Nil

    def printNode(self):
        print(self.value , tree_height(self))                
class Nil:
    value = None
    red = False # if false then black
    parent = None
    right = None
    left = None
