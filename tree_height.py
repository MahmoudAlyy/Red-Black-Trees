def tree_height(node):
    if node == None:
        return 0
    return max(1 + tree_height(node.left), 1 + tree_height(node.right))    
