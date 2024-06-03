'''
입력
N = 5
[8, 3, 7, 9, 2]

M = 3
[5, 7, 9]
'''

# 시간복잡도 : O((M+N)logN)
# 1. 입력
import sys

N = int(input())
n1 = list(sys.stdin.readline().rstrip())

M = int(input())
m1 = list(sys.stdin.readline().rstrip())

answer = list()
# 2. 데이터 정렬
n1.sort()

# 3. 탐색
start = n1[0]
end = n1[-1]
mid = n1[N //2]

def search_binary(target, start, end):
    while start <= end:
        if n1[mid] == target:
           return mid
        elif n1[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

for i in m1:
    result = search_binary(i, start, end)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')



# 방법 2.계수 정렬

n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes' , end=' ')
    else:
        print('no', end=' ')


# 방법 3. 집합 자료형
# 해시테이블을 사용하여 특정한 데이터가 존재하는지 검사할 때 효과적으로 사용가능!
# 시간복잡도 O(m)

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

















