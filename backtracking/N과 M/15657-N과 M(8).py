import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
arr = list()
num.sort()

def func(k):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(k, n):
        arr.append(num[i])
        func(i)
        arr.pop()
func(0)