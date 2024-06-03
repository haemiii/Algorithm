n, m = map(int, input().split())
arr = list()


def func(k):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(k, n+1):
        if i not in arr:
            arr.append(i)
            func(i+1)
            arr.pop()

func(1)