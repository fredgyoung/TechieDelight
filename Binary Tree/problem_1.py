

class Node:

    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def is_identical(x, y):

    # If both trees are empty, return True
    if not x and not y:
        return True

    # If both trees are non-empty and the values of their root nodes match
    # recursively check their chilcren
    return (x and y) and \
        x.key == y.key and \
        is_identical(x.left, y.left) and \
        is_identical(x.right, y.right)

if __name__ == '__main__':

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

