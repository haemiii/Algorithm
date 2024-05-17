n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = list()
def func():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(n):
        if num[i] not in arr:
            arr.append(num[i])
            func()
            arr.pop()
func()