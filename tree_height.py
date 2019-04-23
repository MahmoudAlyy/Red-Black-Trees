from Node import *
from Tree import *
def tree_height(node):
    if node == None or node == Nil: #added Nil and switched from -1 to -
         return 0 
    return max(1 + tree_height(node.left), 1 + tree_height(node.right))
def node_height(tree,node) : #abort
     t_h = tree_height(tree.root)
     n_h = tree_height(node)
     return (t_h - n_h +1)