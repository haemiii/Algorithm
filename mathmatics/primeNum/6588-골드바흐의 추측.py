# '''
# [입력]
# 8
# 20
# 42
# 0
# '''
# import math
# import sys
# import time
#
# n = 1000000
# arr = [True for _ in range(n+1)]
# arr[1] = False
#
# for i in range(2, `780int(math.sqrt(n))+1):
#     if arr[i]:
#         j = 2
#         while i*j <= n:
#             arr[i*j] = False
#             j += 1
#
# while True:
#     N = int(sys.stdin.readline())
#     cnt = 0
#
#     if N == 0:
#         break
#     for i in range(3, (N//2)+1, 2):
#         if arr[i] and arr[N-i]:
#             print(f"{N} = {i} + {N-i}")
#             cnt += 1
#             break
#     if cnt == 0:
#         print("Goldbach's conjecture is wrong.")
#
