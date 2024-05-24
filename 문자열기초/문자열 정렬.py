from functools import cmp_to_key
num = list(map(str, input().split()))

print(num)

def compare_max(x, y):
    print("x, y", x, y)
    if x+y > y+x:
        return -1
    else:
        return 1


sorted_min = sorted(num, key=cmp_to_key(compare_max))
print(sorted_min)