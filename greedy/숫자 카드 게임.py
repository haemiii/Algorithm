'''
입력값

3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]

max_value = 0
for card_list in cards:
    x = min(card_list)
    if max_value < x:
        max_value = x

print(max_value)

#### 해설 ####

n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)

    result = max(result, min_value)

print(result)