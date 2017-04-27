"""
Write an efficient algorithm to compute the height of binary tree. 
The height or depth of a tree is number of edges or nodes on longest path from root node to leaf node.
"""


class Node:

    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def add_left(self, obj):
        if not self.left:
            self.left = Node(obj)
        else:
            temp = Node(obj)
            temp.left = self.left
            self.left = temp

    def add_right(self, obj):
        if not self.right:
            self.right = Node(obj)
        else:
            temp = Node(obj)
            temp.right = self.right
            self.right = temp


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