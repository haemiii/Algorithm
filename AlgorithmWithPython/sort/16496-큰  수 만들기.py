from functools import cmp_to_key

n = int(input())
num = list(map(str, input().split()))

def max_value(x, y):
    if x+y > y+x:
        return -1
    elif x+y < y+x:
        return 1
    else:
        return 0

sorted_value = sorted(num, key=cmp_to_key(max_value))
result = ''.join(sorted_value)

# 000일떄 -> 0으로 출력!
if result[0] == '0':
    result = '0'

print(result)
