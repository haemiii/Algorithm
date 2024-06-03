# a + b = x가 되는 (a, b)쌍의 개수
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
x = int(input())

'''
cnt_num = [0] * 1000001
for i in num:
    cnt_num[i] += 1
cnt = 0

num.sort()
for i in range(1, (x//2)+1):
    if i <= 1000000 and (x - i) <= 1000000 and cnt_num[i] + cnt_num[x-i] == 2 and i != x-i:
        print(i, x-i)
        cnt += 1

print(cnt)
'''

# 투 포인터로 풀이
# 특정 조건을 만족하는 쌍, 부분 배열 찾기 -> 정렬되어 있을때 사용하기 좋다!
num.sort()

left = 0
right = n - 1
count = 0

while left < right:
    current_sum = num[left] + num[right]
    if current_sum == x:
        count += 1
        left += 1
        right -= 1
    elif current_sum <x:
        left += 1
    else:
        right -= 1
print(count)