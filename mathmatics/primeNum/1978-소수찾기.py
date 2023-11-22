import math
N = 1000
n = int(input())
isPrime = list(map(int, input().split()))
arr = [True for _ in range(N+1)]

arr[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    if arr[i]:
        j = 2
        while i * j <= N:
            arr[i*j] = False
            j += 1

cnt = 0
for i in isPrime:
    if arr[i]:
        cnt += 1
print(cnt)