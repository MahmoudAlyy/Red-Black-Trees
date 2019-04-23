from Node import *
from Tree import *

"""
def inOrderSuccessor(node): # Normal Successor
    if node.right != Nil:
        succ = node.right
        while succ.left != Nil :
            succ = succ.left
        return succ
    else :
        return node

"""
def inOrderSuccessor(node):  # predecessor for testing
    if node.left != Nil:
        succ = node.left
        while succ.right != Nil:
            succ = succ.right
        return succ
    else:
        return node

def replaceV2 (source , target): 
    target.value = source.value

