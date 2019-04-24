from Node import *
from Tree import *
from DelMeWelpFunc import *


def DelMe(tree, node):
    if node.value == None :
        print('ERROR!Word doesn\'t exist in the tree\n')
        return
    succ = inOrderSuccessor(node)
    print("succ is ")
    succ.printNode()
    replaceV2(succ, node)
    dd = None
    
    if succ.red == True:  # case 1 : Node red  #red nodes always have black chil
        if succ.right != Nil:
            succ.value = succ.right.value  # value
            succ.right = Nil
        elif succ.left != Nil:
            succ.value = succ.left.value
            succ.left = Nil
        else:
            if succ == succ.parent.left:
                succ.parent.left = Nil
            elif succ == succ.parent.right:
                succ.parent.right = Nil
        print("case1 done")

    # case 2 : Node black but has red children(MUST HAVE A RED CHILD    ) # if a black node has 2 child and 1 is red then the other must be red
    elif succ.red == False and (succ.left.red == True or succ.right.red == True):
        if succ.left.red == True:
            succ.value = succ.left.value
            succ.left = Nil
        elif succ.right.red == True:
            succ.value = succ.right.value
            succ.right = Nil
        print("case 2 done")

    else:  # case 3 : set double Black
        if succ.left != Nil:
            succ.value = succ.left.value
            succ.left = Nil
            dd = succ
        elif succ.right != Nil:
            succ.value = succ.right.value
            succ.right = Nil
            dd = succ
        else:
            print("both child are nil")
            if succ == succ.parent.left:
                #print(succ.value , succ.parent.value , succ.parent.right.value)
                p = succ.parent
                dd = Nil
                p.left = dd
                dd.parent = p
            elif succ == succ.parent.right:
                p = succ.parent
                dd = Nil
                p.right = dd
                dd.parent = p

        print("double black")
        print("dd value = ", dd.value, "dd.parent.value = ",
              dd.parent.value, "dd.parent.right.value = ", dd.parent.right.value)
        Doulbe_Black(tree, dd)
    tree.size-=1
    print("Size is ")
    print(tree.getSize())


def Doulbe_Black(tree, dd):

   while 1:

        if dd == tree.root:
            print("terminal case 1")
            break
        # terminal case 1

        if dd == dd.parent.left:
            sib = dd.parent.right
            #print("test sib right")
        else:
            sib = dd.parent.left
            #print("test sib left")
        # determine sib

        # cases 3,4 are recoloring cases so they dont depend on position of dd relative to its parent

        if (dd.parent.red == False and sib.red == False and sib.left.red == False and sib.right.red == False):
            sib.red = True
            dd = dd.parent
            print("case 3")
        # case 3

        elif (dd.parent.red == True and sib.red == False and sib.left.red == False and sib.right.red == False):
            dd.parent.red = False
            sib.red = True
            print("Terminal case 4")
            break
        # terminal case 4

        # case 2,5,6 are rotating (also have recoloring) cases so they deped on dd position relative to its parent

        elif dd == dd.parent.left:  # dd is a left child

            if (dd. parent.red == False and sib.red == True):
                dd.parent.red = True
                sib.red = False
                left_rotate(tree, sib.parent)
                print("case 2 , dd is left")
            # case 2

            elif (dd.parent.red == False and sib.red == False and (sib.left.red == True and sib.right.red == False)):
               sib.left.red = False
               sib.red = True
               right_rotate(tree, sib)
               print("case 5 , dd is left")
            # case 5

            elif sib.red == False and (sib.right.red == True):
                sib.red = sib.parent.red
                sib.parent.red = False
                sib.right.red = False
                left_rotate(tree, sib.parent)
                print("terminal case 6 , dd is left")
                break
            # terminal case 6

        else:  # dd is a right child

            if (dd. parent.red == False and sib.red == True):
                dd.parent.red = True
                sib.red = False
                right_rotate(tree, sib.parent)
                print("case 2 , dd is right")
            # case 2

            elif (dd.parent.red == False and sib.red == False and (sib.right.red == True and sib.left.red == False)):
               sib.right.red = False
               sib.red = True
               left_rotate(tree, sib)
               print("case 5 , dd is right")
            # case 5

            elif sib.red == False and (sib.left.red == True):
                sib.red = sib.parent.red
                sib.parent.red = False
                sib.left.red = False
                right_rotate(tree, sib.parent)
                print("terminal case 6 , dd is right")
                break
            # terminal case 6

        # 2ai 7aaga fiha rotate lazm yb2a liha mirror
        # case 5 and 6 and 2 need mirror
