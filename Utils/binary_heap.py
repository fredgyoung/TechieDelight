

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

    def heapify_up(self, child):
        parent = child // 2
        if self.queue[parent] < self.queue[child]:
            self.swap(parent, child)

    def swap(self, parent, child):
        temp = self.queue[parent]
        self.queue[parent] = self.queue[child]
        self.queue[child] = temp

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
