'''
입력
4 6
19 15 10 17

출력
15
'''

# import sys
# N, M = map(int, sys.stdin.readline().rstrip().split())
# h = list(map(int, sys.stdin.readline().rstrip().split()))
#
# def cut(size, arr):
#     result = 0
#     for i in arr:
#         if i - size >= 0:
#             result += i-size
#     return result
#
# def binary_search(arr, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         result = cut(mid, arr)
#         if result == target:
#             return mid
#         elif result > target:
#             start = mid+1
#         else:
#             end = mid -1
#     return None
#
#
# x = binary_search(h, M, 0, max(h))
# print(x)


# # 또 다른 풀이
n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)









































