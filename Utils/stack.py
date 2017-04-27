

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if len(self.stack) == 0:
            return 'Error: Stack Underflow'
        else:
            return self.stack.pop()

    def empty(self):
        return len(self.stack) == 0


if __name__ == '__main__':

    def test_stack():

        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        print(s.empty())
        print(s.pop())
        print(s.pop())
        print(s.pop())
        print(s.pop())
        print(s.empty())


