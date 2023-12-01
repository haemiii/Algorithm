# from _collections import deque
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# deque = deque([i+1 for i in range(N)])
#
# while (len(deque) != 1):
#     deque.popleft()
#     item = deque.popleft()
#     deque.append(item)
#
# print(deque[0])


from _collections import deque
import sys

N = int(input())
deque = deque([i+1 for i in range(N)])

while len(deque) != 1:
    deque.popleft()
    deque.append(deque.popleft())
print(deque[0])

























