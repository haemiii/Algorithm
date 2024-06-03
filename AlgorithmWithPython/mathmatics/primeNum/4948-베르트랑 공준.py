import math

N = 123456*2
arr = [True for _ in range(N+1)]
arr[1] = False

for i in range(2, int(math.sqrt(N))+1):
    if arr[i]:
        j = 2
        while i*j <= N:
            arr[i*j] = False
            j += 1

def isPrime(n):
    cnt = 0
    for i in range(n+1, 2*n + 1):
        if arr[i]:
            cnt += 1
    return cnt

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(isPrime(n))
