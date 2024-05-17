n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = list()
visited = [False] * n

def func():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    prev = -1
    for i in range(n):
        if num[i] != prev and not visited[i]:
            visited[i] = True
            arr.append(num[i])
            prev = num[i]
            func()
            visited[i] = False
            arr.pop()
func()