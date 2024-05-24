import sys
input = sys.stdin.readline

n = int(input())
arr = [0]*10001

for i in range(n):
    x = int(input())
    arr[x] += 1

for j, v in enumerate(arr):
    if n == 0:
        break
    if v != 0:
        for i in range(v):
            print(j)
            n -=1


