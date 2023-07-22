import sys

class Stack:
    def __init__(self):
        self.list = []

    def push(self, x):
        self.list.append(x)

    def pop(self):
        if self.size() == 0:
            return -1
        return self.list.pop()

    def size(self):
        return len(self.list)

    def empty(self):
        if self.size() == 0:
            return 1
        return 0

    def top(self):
        if self.size() == 0:
            return -1
        return self.list[-1]


n = int(sys.stdin.readline())
stack = Stack()

for i in range(n):
    command = list(sys.stdin.readline().split())

    if command[0] == "push":
        n = int(command[1])
        stack.push(n)
    elif command[0] == "pop":
        print(stack.pop())
    elif command[0] == "size":
        print(stack.size())
    elif command[0] == "empty":
        print(stack.empty())
    elif command[0] == "top":
        print(stack.top())