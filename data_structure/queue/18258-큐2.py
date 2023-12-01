import sys
class Queue:
    def __init__(self):
        self.q = list()
        self.front_index = 0
    def push(self, val):
        self.q.append(val)
    def pop(self):
        if len(self.q) == 0 or self.front_index == len(self.q):
            return -1
        x = self.q[self.front_index]
        self.front_index += 1
        return x
    def size(self):
        return len(self.q) - self.front_index
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
    def front(self):
        if self.size() == 0:
            return -1
        return self.q[self.front_index]
    def back(self):
        if self.size() == 0:
            return -1
        return self.q[-1]
N = int(input())
queue = Queue()
for i in range(N):
    sen = list(sys.stdin.readline().split())
    if sen[0] == 'push':
        queue.push(int(sen[1]))
    elif sen[0] == 'pop':
        print(queue.pop())
    elif sen[0] == 'size':
        print(queue.size())
    elif sen[0] == 'empty':
        print(queue.empty())
    elif sen[0] == 'front':
        print(queue.front())
    else:
        print(queue.back())