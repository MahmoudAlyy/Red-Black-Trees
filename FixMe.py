from Node import *
from Tree import *


def fixme(RBtree, node):
    while node.parent != None and node.parent.red == True:
        if node.parent == node.parent.parent.left:  # case where uncle on right
            uncle = node.parent.parent.right

            if uncle.red:  # uncle red so we do color flip
                node.parent.red = False
                uncle.red = False
                node.parent.parent.red = True
                # might need to be fixed bec the inserted node grandparent may have a parent who is red. # error when this points to the root FIXED
                node = node.parent.parent

            else:  # uncle black so we rotate
                # if inserted node is on the right & (Unlce was on the right) we do left the right rotation
                if node == node.parent.right:
                    node = node.parent
                    left_rotate(RBtree, node)
                # if inserted node on the left & (Unlce was on the right) we do right rotation only
                node.parent.red = False
                node.parent.parent.red = True
                right_rotate(RBtree, node.parent.parent)

        # case where uncle is on left (mirror of above code)
        else:
            uncle = node.parent.parent.left

            if uncle.red:
                node.parent.red = False
                uncle.red = False
                node.parent.parent.red = True
                node = node.parent.parent

            else:
                if node == node.parent.left:
                    node = node.parent
                    right_rotate(RBtree, node)
                node.parent.red = False
                node.parent.parent.red = True
                left_rotate(RBtree, node.parent.parent)

    RBtree.root.red = False  # root of tree must be black


def left_rotate(RBtree, node):
    sibling = node.right
    node.right = sibling.left
    #Turn sibling's left subtree into node's right subtree
    if sibling.left != None:
        sibling.parent = node.parent
    sibling.left.parent = node
    if node.parent == None:
        RBtree.root = sibling
    else:
        if node == node.parent.left:
            node.parent.left = sibling
        else:
            node.parent.right = sibling
    sibling.left = node
    node.parent = sibling


def right_rotate(RBtree, node):  # mirror of left_rotate
    sibling = node.left
    node.left = sibling.right
    if sibling.right != None:
        sibling.right.parent = node
    sibling.parent = node.parent
    if node.parent == None:
        RBtree.root = sibling
    else:
        if node == node.parent.right:
            node.parent.right = sibling
        else:
            node.parent.left = sibling
    sibling.right = node
    node.parent = sibling
