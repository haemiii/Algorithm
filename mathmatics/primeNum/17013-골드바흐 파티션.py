import math
import sys

# 소수 구하기
N = 1000000
arr = [True for _ in range(N+1)]
arr[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    if arr[i]:
        j = 2
        while i*j <= N:
            arr[i*j] = False
            j += 1

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    cnt = 0
    for j in range(2, (n//2)+1):
        if arr[j] and arr[n-j]:
            cnt += 1

    print(cnt)