from Node import *
def tree_height(node):
    if node == None or node == Nil: #added Nil and switched from -1 to -
         return 0 
    return max(1 + tree_height(node.left), 1 + tree_height(node.right))
