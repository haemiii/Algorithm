import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
d = [0] * 100001
d[0] = 0
for i in range(1, n+1):
    d[i] = d[i-1] + num[i-1]

for k in range(m):
    i, j = map(int, input().split())
    print(d[j]-d[i-1])
