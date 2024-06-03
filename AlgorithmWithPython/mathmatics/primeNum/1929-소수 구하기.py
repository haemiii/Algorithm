import math

# 에라토스테네스의 체
M, N = map(int, input().split())

arr = [True for _ in range(N+1)]
arr[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    if arr[i]:
        j = 2
        while i*j <= N:
            arr[i*j] = False
            j += 1

for i in range(M, N+1):
    if arr[i]:
        print(i)
