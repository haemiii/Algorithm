n, s = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = []
cnt = 0

def func(k):
    global cnt
    if sum(arr) == s and len(arr) != 0:
        cnt += 1
    for i in range(k, n): # n>k 일때만 루프 수행!
            arr.append(num[i])
            func(i+1)
            arr.pop()
func(0)
print(cnt)