'''

N : 개수
S : 정수

nums의 부분수열의 합 = S
'''

# N, S = map(int, input().split())
# nums = list(map(int, input().split()))
#
# p = []
# cnt = 0
#
# def sequence(k):
#     global cnt
#
#     print(p)
#     if p and sum(p) == S:
#         cnt += 1
#
#     for i in range(k, N):
#         p.append(nums[i])
#         sequence(i+1)
#         p.pop()
#
# sequence(0)
# print(cnt)


## 라이브러리를 사용해보자!! : permutation()

from itertools import combinations, permutations

N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

for i in range(1, N+1):
    for comb in combinations(nums, i):  # 순서 상관 o
        print(comb)
        if sum(comb) == S:
            cnt += 1
    for per in permutations(nums, i):  # 순서 상관 x
        print(per)
print(cnt)

