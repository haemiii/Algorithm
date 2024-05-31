# 한 세트 : 0~9까지, 6-> 9, 9 -> 6으로 활용가능!
import math
n = list(input())
cnt = [0]*10

for i in n:
    cnt[int(i)] += 1
v = cnt[6] + cnt[9]

cnt[6] = round(v / 2)
cnt[9] = round(v / 2)

print(max(cnt))