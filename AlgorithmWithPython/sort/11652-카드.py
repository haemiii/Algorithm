import sys
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()

max_value = -1e9
max_cnt = 0
cnt = 1
val = num[0]
for i in range(1, n):
    if val == num[i]:
        cnt += 1
    else:
        if max_cnt < cnt:
            max_cnt = cnt
            max_value = num[i-1]
        val = num[i]
        cnt = 1


print(max_value)