'''
입력값

5
2 3 1 2 2

7
1 1 2 2 2 3 3

10
1 2 2 2 3 3 3 3 4 4
'''

import sys
input = sys.stdin.readline

n = int(input())
fear = list(map(int, input().split()))
fear.sort()
cnt = 0

temp = 1
for k in fear:
    if temp == k:
        cnt += 1
        temp = 1
        continue
    temp += 1
print(cnt)

#### 해설 ####
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)