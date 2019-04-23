class Node:
    """ red black tree node class """

    def __init__(self, value):
        self.value = value
        self.red = True # if false then black
        self.parent = None
        self.right = Nil
        self.left = Nil
        

    def printNode(self):
        print(self.value,end = ' ')
        if self.red ==True :
            print("RED")
        else :
            print("BLACK")
class Nil:
    value = None
    red = False  # if false then black
    right = None
    left = None
    parent = None
           

    def printNode(self):
        print(self.value,end = ' ')
        if self.red ==True :
            print("RED")
        else :
            print("BLACK")
