'''
입력값
5
-15 -6 1 3 7

7
-15 -4 2 8 9 14 15

7
-15 -4 3 8 9 13 15
'''

### 선형탐색 -> 시간초과
import sys

# n = int(sys.stdin.readline().rstrip())
# n_list = list(map(int, sys.stdin.readline().rstrip().split()))
#
# flag = 1
# for i, v in enumerate(n_list):
#     if i == v:
#         print(i)
#         flag = 1
#         break
#     flag = -1
#
# if flag == -1:
#     print(-1)

### 이진탐색 수행

def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    else:
        return binary_search(array, mid+1, end)

n = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().rstrip().split()))

result = binary_search(n_list, 0 , n-1)
if result == None:
    print(-1)
else:
    print(result)