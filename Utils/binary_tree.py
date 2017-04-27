

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


