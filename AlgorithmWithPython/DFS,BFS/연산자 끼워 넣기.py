'''
# N개의 수로 이루어진 수열
# N-1개의 연산자 : +-*/
# 주어진 숫자의 순서는 바꾸면 안됨!
연산 조건
1 .앞에서부터
2. 나눗셈은 정수 나눗셈으로 몫만 취함
3. 음수 / 양수 -> 양수 / 양수 = 몫 -> -몫
'''

# 중복 순열 -> 연산자 조합할 때 사용!
# 1. product
'''
from itertools import product

n = 4
print(list(product(['+', '-', '*', '/'], repeat=(n-1))))
'''

# 2. itertools없이 dfs로 구현
n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i == n: # 한사이클의 연산이 완성
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now-data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / data[i]))
            div += 1


dfs(1, data[0])

print(max_value)
print(min_value)