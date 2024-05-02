'''
입력값
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
weight = list(map(int, input().split()))

cnt = 0
for i in range(len(weight)):
    for j in range(i, len(weight)):
        if weight[i] == weight[j]:
            continue
        cnt += 1

print(cnt)


##### 해설 #####

array = [0] * 11
for x in weight:
    array[x] += 1

result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)