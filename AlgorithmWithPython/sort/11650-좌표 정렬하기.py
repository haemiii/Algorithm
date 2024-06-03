import sys
from functools import cmp_to_key
input = sys.stdin.readline

def sort_location(x, y):
    if x[0] > y[0]:
        return 1
    elif x[0] == y[0]:
        if x[1] >= y[1]:
            return 1
        else:
            return -1
    else:
        return -1


n = int(input())
location = [list(map(int, input().split())) for _ in range(n)]
# 방법 1
# location = sorted(location, key=cmp_to_key(sort_location))
# 방법 2
location = sorted(location, key=lambda x :(x[0], x[1]))

for i in location:
    print(' '.join(map(str, i)))

