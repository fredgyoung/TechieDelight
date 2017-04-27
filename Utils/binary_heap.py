

class BinaryHeap:

    def __init__(self):
        self.queue = [None]

    def push(self, obj):
        self.queue.append(obj)

    def pop(self):
        if len(self.queue) > 1:
            return self.queue.pop()
        else:
            return None

    def peek(self):
        return self.queue[-1]

    def heapify_up(self):
        pass

    def heapify_down(self):
        pass

    # parent = child // 2
    # left child = parent * 2
    # right child = (parent * 2) + 1


if __name__ == '__main__':

    h = BinaryHeap()
    h.push(3)
    print(h.peek())
    print(h.pop())
    print(h.pop())
