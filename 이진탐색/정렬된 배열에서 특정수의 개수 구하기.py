'''
입력값
7 2
1 1 2 2 2 2 3


# list.count() -> O(N) : 순차탐색x
# O(logN) -> 이진탐색

'''
# 이진탐색 -> 처음과 끝을 찾아내야한다!
import sys

# n, x = map(int, sys.stdin.readline().rstrip().split())
# n_list = list(map(int, sys.stdin.readline().rstrip().split()))
#
# start = 0
# end = n - 1
#
# left = start
# right = end
# cnt = 0
# while start <= end:
#     if n_list[end] < x:
#         print(-1)
#         break
#
#     mid = (start + end) // 2
#     if n_list[mid] < x:
#         left = mid
#         start = mid + 1
#     elif n_list[mid] > x:
#         right = mid
#         end = mid - 1
#     else:
#         cnt = n_list[left: right+1].count(x)
#         print(cnt)
#         break


## 처음 인덱스구하는 이진탐색, 마지막 인덱스 구하는 이진탐색

def count_by_value(array, x):
    n = len(array)

    a = first(array, x, 0, n-1)

    if a == None:
        return 0
    b = last(array, x, 0, n-1)

    return b-a+1

def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if(mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid -1)
    else:
        return first(array, target, mid+1, end)

def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if(mid == n-1 or target < array[mid+1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return first(array, target, start, mid -1)
    else:
        return first(array, target, mid+1, end)

n, x = map(int, sys.stdin.readline().rstrip().split())
n_list = list(map(int, sys.stdin.readline().rstrip().split()))

count = count_by_value(n_list, x)

if count == 0:
    print(-1)
else:
    print(count)

## bisect 라이브러리 사용 -> 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구할 수 있다!

from bisect import bisect_left, bisect_right

n, x = map(int, sys.stdin.readline().rstrip().split())
n_list = list(map(int, sys.stdin.readline().rstrip().split()))

def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)

    return right_index - left_index


count = count_by_range(n_list, x, x)

if count == 0:
    print(-1)
else:
    print(count)