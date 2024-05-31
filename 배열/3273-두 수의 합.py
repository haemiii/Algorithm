# a + b = x가 되는 (a, b)쌍의 개수
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
x = int(input())

cnt_num = [0] * 100001
for i in num:
    cnt_num[i] += 1
cnt = 0

num.sort()
for i in num:
    if i >= x:
        break
    if cnt_num[x-i] != 0:
        cnt_num[x-i] = 0
        cnt_num[i] = 0
        cnt += 1

print(cnt)