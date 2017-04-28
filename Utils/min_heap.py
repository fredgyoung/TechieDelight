

class MinHeap:

    def __init__(self):
        self.stack = [0]
        self.current_size = 0

    def insert(self, obj):
        self.stack.append(obj)
        self.current_size += 1
        self.heapify_up(self.current_size)

    def heapify_up(self, index):
        while (index // 2) > 0:
            mc = self.min_child(index)
            if self.stack[index] > self.stack[mc]:
                temp = self.stack[index]
                self.stack[index] = self.stack[mc]
                self.stack[mc] = temp
            index = mc

    def heapify_down(self, index):
        while (index * 2) <= self.current_size:
            if self.stack[index] < self.stack[index // 2]:
                temp = self.stack[index // 2]
                self.stack[index // 2] = self.stack[index]
                self.stack[index] = temp
            index = index // 2

    def min_child(self, index):
        if index * 2 + 1 > self.current_size:
            return index * 2
        else:
            if self.stack[index * 2] < self.stack[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def del_min(self):
        pass

    def build_heap(self):
        pass

if __name__ == '__main__':

    mh = MinHeap()
