n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

arr = list()

def func(k):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(k, n):
        if num[i] not in arr:
            arr.append(num[i])
            func(i+1)
            arr.pop()
func(0)


