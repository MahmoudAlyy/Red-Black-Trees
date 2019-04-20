from Node import *
def inOrderSuccessor(node): #ezi
    if node.right != Nil:
        succ = node.right
        while succ.left != Nil :
            succ = succ.left
        return succ
    else :
        return node
"""
def replace (soruce , target):
    if target = target.parent.left :
        p = target
    p = target.parent
    l = target.left
    r = targe.right
"""
