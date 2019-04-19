from Node import *
def tree_height(node):
    if node == None:
        return -1
    return max(1 + tree_height(node.left), 1 + tree_height(node.right))    
