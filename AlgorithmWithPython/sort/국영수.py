'''입력값
12
Junkyu 50 60 100
Sankeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Doonghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
'''

import sys

N = int(sys.stdin.readline())
score = []

# 입력
for i in range(N):
    score.append(sys.stdin.readline().rstrip().split())

score.sort(key=lambda x: (-int(x[1]), int(x[2]), (-int(x[3])), x[0]))

for i in score:
    print(i[0])


