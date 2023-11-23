# 소수
import math
import sys

n = 10000
arr = [True for _ in range(n+1)]
arr[1] = False

for i in range(2, int(math.sqrt(n))+1):
    if arr[i]:
        j = 2
        while i*j <= n:
            arr[i*j] = False
            j += 1


N = int(sys.stdin.readline())

for i in range(N):
    N = int(sys.stdin.readline())
    for j in range(N//2, 1, -1):
        if arr[j] and arr[N-j]:
            print(j, N-j)
            break