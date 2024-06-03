# import sys
#
# k = int(input())  # k개의 정수가 주어질 것!
# stack = []
#
# for i in range(k):
#     n = int(sys.stdin.readline())
#
#     if n == 0:
#         stack.pop()
#     else:
#         stack.append(n)
#
# sum = 0
# for j in stack:
#     sum += j
# print(sum)


# 제로
import sys
K = int(sys.stdin.readline())
s = list()
for i in range(K):
    n = int(sys.stdin.readline())

    if n == 0:
        s.pop()
    else:
        s.append(n)

print(sum(s))

















