class Node:
    """ red black tree node class """
    RED = 'red'
    BLACK = 'black'

    def __init__(self, value=0, color=RED, parent=None, right=None, left=None):
        self.value = value
        self.color = color
        self.parent = parent
        self.right = right
        self.left = left

    def f(self):
        return 'hello world from Node'
