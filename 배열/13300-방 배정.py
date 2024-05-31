# 성별, 학년
# 여학생 : 0, 남학생 1
# 같은 학년끼리, 같은 성별끼리
import math
n, k = map(int, input().split())
std = [[0]*2 for _ in range(6)]

for i in range(n):
    s, y = map(int, input().split())
    std[y-1][s] += 1

room = 0
for i in std:
    room += math.ceil(i[0] / k)
    room += math.ceil(i[1] / k)

print(room)
