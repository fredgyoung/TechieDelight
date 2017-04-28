

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

    def swap(self, parent, child):
        temp = self.queue[parent]
        self.queue[parent] = self.queue[child]
        self.queue[child] = temp


if __name__ == '__main__':

    h = BinaryHeap()
    h.push(3)
    print(h.peek())
    print(h.pop())
    print(h.pop())
