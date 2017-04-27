"""
Write an efficient algorithm to compute the height of binary tree. 
The height or depth of a tree is number of edges or nodes on longest path from root node to leaf node.
"""

from Utils.binary_tree import Node

# Recursive
def height(x):

    # If no children return 0
    if not x:
        return 0

    # Traverse
    return max(height(x.left), height(x.right)) + 1


tree = Node(1)
tree.add_left(4)
tree.add_right(3)
tree.add_left(2)
tree.add_right(3)
tree.add_right(3)
tree.add_right(3)
tree.add_right(3)
tree.add_right(3)
tree.add_right(3)


print(height(tree))