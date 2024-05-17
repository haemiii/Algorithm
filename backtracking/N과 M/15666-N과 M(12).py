n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = list()

def func(k):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    prev = -1
    for i in range(k, n):
        if num[i] != prev:
            arr.append(num[i])
            prev = num[i]
            func(i)
            arr.pop()
func(0)