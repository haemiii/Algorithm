import sys

N = int(input())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

arr = sorted(arr, reverse=True)

for i in arr:
    print(i, end=" ")