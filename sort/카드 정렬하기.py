'''
N = int(input())
card = []

for i in range(N):
    card.append(int(input()))
card.sort()

result = []
if len(card) == 1:
    print(card[0])
else:
    result.append(card[0]+card[1])
    for i in range(2, len(card)):
        result.append(result[i-2]+card[i])

    print(sum(result))
'''

'''
i , i+1, i+2 i+3
10, 20, 40, 50

i+i+1, 
30(10+20) , 70(30+40), 120(30+40+50)

'''
# heap 자료구조를 이용한 우선순위 큐!
import heapq

n = int(input())
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)