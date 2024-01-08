from _collections import deque

N, M = map(int, input().split())
nums = deque(map(int, input().split()))
cnt = 0

'''
    1
 2     5
  3  4

'''

while len(nums) != 0:
    index = 1
    if index == nums[0]:
        nums.popleft()
    else:
        index += 1
        index %= 10
