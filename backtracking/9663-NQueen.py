# N*N 체스판에 퀸 N개를 서로 공격할 수 없게 놓는 문제

n = int(input())
cnt = 0

isused1 = [False] * n
isused2 = [False] * (2*n)
isused3 = [False] * (2*n)

def func(cur):
    global cnt
    if cur == n:
        cnt += 1
        return
    for i in range(n):
        if isused1[i] or isused2[cur+i] or isused3[cur-i+n-1]:
            continue
        isused1[i] = 1
        isused2[cur+i] = 1
        isused3[cur-i+n-1] = 1
        func(cur+1)
        isused1[i] = 0
        isused2[cur+i] = 0
        isused3[cur-i+n-1] = 0


func(0)
print(cnt)

