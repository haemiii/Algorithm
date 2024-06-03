from functools import cmp_to_key
import sys
input = sys.stdin.readline

num = set('0123456789')

def sum_value(arr):
    return sum(int(i) for i in arr if i in num)

def serial_sort(x, y):
    if len(x) != len(y):
        return len(x) - len(y)

    sum_x = sum_value(x)
    sum_y = sum_value(y)
    if sum_x != sum_y:
        return sum_x - sum_y

    return (x>y) - (x<y)


n = int(input())
serial = [input().rstrip() for _ in range(n)]
serial = sorted(serial, key=cmp_to_key(serial_sort))

for i in serial:
    print(i)