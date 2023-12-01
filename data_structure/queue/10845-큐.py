# import sys
#
# class Queue:
#     def __init__(self):
#         self.queue = []
#         self.qfront = 0
#         self.rear = 0
#
#     def push(self, key):
#         self.queue.append(key)
#         self.rear += 1
#
#     def pop(self):
#         if self.empty() == 1:
#             return -1
#         else:
#             p = self.queue[self.qfront]
#             self.qfront += 1
#             return p
#
#     def front(self):
#         if self.empty():
#             return -1
#         return self.queue[self.qfront]
#
#     def back(self):
#         if self.empty():
#             return -1
#         return self.queue[-1]
#
#     def size(self):
#         return len(self.queue) - self.qfront
#
#     def empty(self):
#         if self.qfront == self.rear:
#             return 1
#         return 0
#
# queue = Queue()
#
# N = int(input())
# for i in range(N):
#     command = sys.stdin.readline().split()
#
#     if command[0] == "push":
#         queue.push(int(command[1]))
#     elif command[0] == "pop":
#         print(queue.pop())
#     elif command[0] == "front":
#         print(queue.front())
#     elif command[0] == "back":
#         print(queue.back())
#     elif command[0] == "size":
#         print(queue.size())
#     elif command[0] == "empty":
#         print(queue.empty())
































