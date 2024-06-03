'''내가 작성한 코드
import sys

N = int(sys.stdin.readline())
location = list(map(int, sys.stdin.readline().rstrip().split()))

location.sort()

distance = []
for i in location:
    sum = 0
    for j in location:
        sum += abs(i-j)
    distance.append([i,sum])

distance.sort(key = lambda x:x[1])
print(distance[0][0])
'''

n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n-1)//2])