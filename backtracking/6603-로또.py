# 방법1
# def func(n):
#     if len(arr) == 6:
#         print(' '.join(map(str, arr)))
#         return
#     for i in range(n, k):
#         if num_list[i] not in arr:
#             arr.append(num_list[i])
#             func(i+1)
#             arr.pop()
#
# while True:
#     x = list(map(int, input().split()))
#     if sum(x) == 0:
#         break
#     else:
#         k = x[0]
#         num_list = x[1:]
#         arr = []
#         func(0)
#         print()

# 방법2
from itertools import combinations

while True:
    x = list(map(int, input().split()))
    if sum(x) == 0:
        break
    else:
        k = x[0]
        num_list = x[1:]
        for i in combinations(num_list, 6):
            print(' '.join(map(str, list(i))))
        print()