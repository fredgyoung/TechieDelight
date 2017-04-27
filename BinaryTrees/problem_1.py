"""
Write an efficient algorithm to check if two binary trees are identical or not. 
i.e. if they have identical structure & their contents are also same.
"""

from Utils.binary_tree import Node
from Utils.stack import Stack


# Recursive solution
def is_identical(x, y):
    # If both trees are empty, return True
    if not x and not y:
        return True

    # If both trees are non-empty and the values of their root nodes match
    # recursively check their children
    return (x and y) and \
           x.key == y.key and \
           is_identical(x.left, y.left) and \
           is_identical(x.right, y.right)


# Iterative solution
def is_identical_2(x, y):
    # If both trees are empty, return True
    if not x and not y:
        return True

    # If the first tree is empty (and second tree is not empty), return False
    if not x:
        return False

    # If the second tree is empty (and first tree is not empty), return False
    if not y:
        return False

    # Create a stack to hold Node pairs
    stack = Stack()
    stack.push((x, y))

    # Do till stack is not empty
    while not stack.empty():
        # pop top pair from stack
        x, y = stack.pop()

        # if the value of their root nodes don't match, return false
        if x.key != y.key:
            return False

        # if left subtree of both x and y exists, push them onto the stack
        # else return false if only one left child exists
        if x.left and y.left:
            stack.push((x.left, y.left))
        elif x.left or y.left:
            return False

        # if right subtree of both x and y exists, push them onto the stack
        # else return false if only one right child exists
        if x.right and y.right:
            stack.push((x.right, y.right))
        elif x.right or y.right:
            return False

    # if we reach here both binary trees are identical
    return True


def test_recursive():
    x = Node(key=1)
    x.left = Node(key=2)
    x.right = Node(key=3)

    y = Node(key=1)
    y.left = Node(key=2)
    y.right = Node(key=3)

    print(is_identical(x, y))

    del x, y

    x = Node(key=1)
    x.left = Node(key=2)
    x.right = Node(key=3)

    y = Node(key=1)
    y.left = Node(key=3)
    y.right = Node(key=2)

    print(is_identical(x, y))


def test_iterative():
    x = Node(key=1)
    x.left = Node(key=2)
    x.right = Node(key=3)

    y = Node(key=1)
    y.left = Node(key=2)
    y.right = Node(key=3)

    print(is_identical_2(x, y))

    del x, y

    x = Node(key=1)
    x.left = Node(key=2)
    x.right = Node(key=3)

    y = Node(key=1)
    y.left = Node(key=3)
    y.right = Node(key=2)

    print(is_identical_2(x, y))


if __name__ == '__main__':

    test = 1
    if test == 1:
        test_recursive()
    elif test == 2:
        test_iterative()
