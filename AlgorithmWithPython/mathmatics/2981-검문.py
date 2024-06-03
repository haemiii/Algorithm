## 시간초과!

# import sys
#
# N = int(sys.stdin.readline())
# num = list()
# for i in range(N):
#     num.append(int(sys.stdin.readline()))
#
# num = sorted(num)
#
#
# for i in range(2, num[0]+1):
#     cnt = 0
#     remain = list()
#
#     for j in range(N):
#         remain.append(num[j] % i)
#
#     if sum(remain) == remain[0]*len(num):
#         print(i, end=" ")

'''
(N- 나머지) % M = 0

나머지를 뺀 값이 모두 M의 배수다!
입력 :
3
6
34
38

출력 :
2 4

m = 2
    6 // 2 : 0
    34 // 2 : 0
    38 // 2 : 0

m = 3
    6 // 3 : 0
    34 // 3 : 1
    38 // 3 : 2

m = 4
    6 // 4 : 2
    34 // 4 : 2
    38 // 4 : 2

m = 5
    6 // 5 : 1
    34 // 5 : 4
    38 // 5 : 3

m = 6
    6 // 6 : 0
    34 // 6 : 4
    38 // 6 : 2
'''
'''
입력 :
3
6 
36
216 

출력 :
2 3 5 6 10 15
정답:
2 3 5 6 10 15 30

입력 :
5
5
17
23
14
83

출력 : 
3
'''

## 문제점 : 만약 num[i]값들이 크다면, 반복문의 횟수가 증가하여 시간초과!
## m 값이 의미하는 바가 도대체 뭘까..?
## -> 어떻게 해결해야할까? : 미해결 ㅜ.ㅜ
import sys

N = int(sys.stdin.readline())
num = list()
for i in range(N):
    num.append(int(sys.stdin.readline()))

num = sorted(num)
m = list()

for i in range(2, num[1]+1):
    cnt = 0
    remain = num[0] % i

    for j in range(1, N):
        if num[j] % i != remain:
            cnt += 1
            break
    if cnt == 0:
        print(i, end=" ")
