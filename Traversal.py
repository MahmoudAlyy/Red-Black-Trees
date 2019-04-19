from Tree import *
from Node import *
from tree_height import *
def postorder(thing):
    if thing != Nil:
        postorder(thing.left)
        postorder(thing.right)
        thing.printNode()
 
def inorder(thing):
    if thing != Nil:
        inorder(thing.left)
        thing.printNode()
        inorder(thing.right)

def printLevelOrder(root): 
    h = tree_height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i) 
  
  
# Print nodes at a given level 
def printGivenLevel(root , level): 
    if root is None or root is Nil: 
        return
    if level == 1: 
        root.printNode(), 
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1) 