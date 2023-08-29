# 1. 이분검색 : 로그 n

'''
8 32
23 87 65 12 57 32 99 81
'''

# N, M = map(int, input().split())
# num = list(map(int, input().split()))
# num.sort()
#
# start = 0
# end = N - 1
#
# while start <= end:
#     mid = (start + end) // 2
#     if num[mid] > M:
#         end = mid-1
#     elif num[mid] < M:
#         start = mid + 1
#     else:
#         print(mid+1)
#         break


# 2. 랜선자르기(결정알고리즘)

'''
4 11
802
743
457
539
'''

K, N = map(int, input().split())
