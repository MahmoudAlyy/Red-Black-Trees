from Node import *
from Tree import *
from DelMeWelpFunc import *

def DelMe(node):
    succ = inOrderSuccessor(node)
    #succ.printNode()
    #replace(succ,node)
    node.value = succ.value
    #succ = tree.searchAndReturn(succ.value)
    if succ.red == True : #case 1
        if succ.left != Nil : #if it has left child
            if succ == succ.parent.left : #if it was on the left of the 
                p = succ.parent
                p.left = Nil
            succ = succ.left
            print("wtf left")
        elif succ.right != Nil :
            succ = succ.right
            print("wtf right")
        else:
            if succ == succ.parent.left :
                p = succ.parent
                p.left = Nil
            print("wtf Nil")
