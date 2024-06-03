n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = list()

def func():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    prev = -1
    for i in range(n):
        if num[i] != prev:
            arr.append(num[i])
            prev = num[i]
            func()
            arr.pop()
func()