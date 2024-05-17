n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

visited = [False]*n
arr = list()

def func(k):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    prev = -1
    for i in range(k, n):
        if not visited[i] and num[i] != prev:
            visited[i] = True
            arr.append(num[i])
            prev = num[i]
            func(i+1)
            visited[i] = False
            arr.pop()
func(0)