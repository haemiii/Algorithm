n, m = map(int, input().split())
num = list(map(int, input().split()))
arr = list()
num.sort()

def func():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(n):
        arr.append(num[i])
        func()
        arr.pop()
func()