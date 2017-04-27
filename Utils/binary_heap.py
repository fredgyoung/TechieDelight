

class BinaryHeap:

    def __init_(self):
        self.queue = [0]

    def push(self, obj):
        self.queue.append(obj)

    def pop(self):
        if len(self.queue) > 1:
            return self.queue.pop()

    def peek(self):
        if len(self.queue) > 1:
            return self.queue[-1]

    def heapify_up(self):
        pass

    def heapify_down(self):
        pass

    # parent = child // 2
    # left child = parent * 2
    # right child = (parent * 2) + 1


if __name__ == '__main__':

