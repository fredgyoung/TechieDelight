

class BinaryHeap:

    def __init__(self):
        self.stack = [0]
        self.current_size = 0

    def insert(self, obj):
        self.stack.append(obj)
        self.current_size += 1


if __name__ == '__main__':

    bh = BinaryHeap()
