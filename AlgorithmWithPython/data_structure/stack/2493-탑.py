# 시간 초과!!

# import sys
#
# N = int(input())
# T = list(map(int, sys.stdin.readline().split()))
# s = [0]
# for i in range(1, N):
#     n = i - 1
#     for j in T[i-1::-1]:
#         if j >= T[i]:
#             s.append(n+1)
#             break
#         n -= 1
#     if n == -1:
#         s.append(0)
# print(' '.join(map(str, s)))

import sys

N = int(input())
T = list(map(int, sys.stdin.readline().split()))
s = [0]

for i in range(1, N):
    if T[i-1] >= T[i]:
        s.append(i)
    else:
        s.append(s[i-1])
print(' '.join(map(str, s)))