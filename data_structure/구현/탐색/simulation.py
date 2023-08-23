# 1. 회문 문자열 검사

'''
len = 5
0  4
1  3
  2
'''

# N = int(input())
# for i in range(N):
#     sentense = list(input().lower())

#     length = len(sentense)
#     for j in range(length // 2):
#         if(sentense[j] != sentense[-1-j]):
#             print("#%d No" %(i+1))
#             break
#     else:
#         print("#%d YES" %(i+1))

## 방법 2.

# N = int(input())
# for i in range(N):
#     sentense = list(input().lower())
#     print(sentense[::-1])

#     length = len(sentense)
#     if sentense == sentense[::-1]:
#         print("#%d YES" %(i+1))
#     else:
#         print("#%d NO" %(i+1))



# 2. 숫자만 추출

# s = input()
# res = 0
# cnt = 0

# for i in s:
#     if i in "0123456789":
#         res = res*10+int(i)
# for i in range(1, res+1):
#     if res % i == 0:
#         cnt += 1
# print(cnt) 

# ## 125
# '''
#     res = 1
#     res = 10 + 2 = 12
#     res = 120 + 5

# '''

# res = 0
# cnt = 0
# for x in s:
#     if x.isdecimal():
#         res = res*10 + int(x)

# for i in range(1, res+1):
#     if res % i == 0:
#         cnt += 1
# print(cnt)




# 3. 카드 역배치
# array = list()
#
#  # 1 ~ 20 까지의 카드
# for i in range(0, 21):
#     array.append(i)
#
#
#  # 10개의 구간
# for i in range(10):
#     inputRange = list(map(int, input().split()))  # 구간
#     mid = (inputRange[0] + inputRange[1]) // 2
#     start = inputRange[0]
#     end = inputRange[1]
#     j = 0
#
#     for i in range(start ,mid):
#         k = array[i]
#         array[i] = array[end - j]
#         array[end-j] = k
#         j += 1
#
# print(array[1:])


# a = list(range(21))
# for _ in range(10):
#     s, e = map(int, input().split()) # 구간
#     for i in range((e-s+1)//2):  # 횟수
#         a[s+i], a[e-i] = a[e-i], a[s+i]
# a.pop(0)
# for x in a:
#     print(x, end=" ")


# 4. 두 리스트 합치기
import sys

# N = int(input())
# array1 = list(map(int, sys.stdin.readline().split()))
# M = int(input())
# array2 = list(map(int, sys.stdin.readline().split()))
#
# arrayPlus = array1 + array2
# print(sorted(arrayPlus))

# N = int(input())
# array1 = list(map(int, sys.stdin.readline().split()))
# M = int(input())
# array2 = list(map(int, sys.stdin.readline().split()))
#
# p1 = p2 = 0
# sortedList = []
# while p1<N and p2< M:
#     if array1[p1] < array2[p2]:
#         sortedList.append(array1[p1])
#         p1 += 1
#     else:
#         sortedList.append(array2[p2])
#         p2 += 1
# if p1 < N:
#     sortedList += array1[p1:]
# if p2 < M:
#     sortedList += array2[p2:]
#
# print(sortedList)


# 5. 수들의 합

# N, M = map(int, input().split())
# num = list(map(int, input().split()))
#
# cnt = 0
# for i in range(len(num)):
#     tot = num[i]
#     for j in num[i+1:]:
#         if M > tot:
#             tot += j
#         if M <= tot:
#             if M == tot:
#                 cnt += 1
#                 tot = 0
#             break
# print(cnt)

# N, M = map(int, input().split())
# num = list(map(int, input().split()))
#
# lt = 0
# rt = 1
# tot = num[0]
# cnt = 0
#
# while True:
#     if tot < M:
#         if rt < N:
#             tot += num[rt]
#             rt +=1
#         else:
#             break
#     elif tot == M:
#         cnt += 1
#         tot -= num[lt]
#         lt += 1
#     else:
#         tot -= num[lt]
#         lt += 1
# print(cnt)

# 6. 격자판 최대합

'''
    아이디어
    1. N * N -> 이중리스트
    2. 격자판에서 나올 수 있는 합의 개수는 ? : 12  = 대각선 2 + 가로 5 + 세로 5
        -> 격자판[0][0] ~ 격자판[0][n-1] : 가로
        -> 격자판[0][0] ~ 격자판[n-1][0] : 세로
        -> 격자판[0][0] ~ 격자판[n-1][n-1] 
           격자판[0][n-1] ~ 격자판[n-1][0]    :대각선
'''

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
largest = 0


def find_max(largest, sum1, sum2):
    if largest < sum1:
        largest = sum1
    if largest < sum2:
        largest = sum2
    return largest


for i in range(N):
    sum1= sum2 = 0
    for j in range(N):
        sum1 += board[i][j]
        sum2 += board[j][i]
    largest = find_max(largest, sum1, sum2)

sum1 = sum2 = 0

for i in range(N):
    sum1 += board[i][i]
    sum2 += board[i][N-i-1]
largest = find_max(largest, sum1, sum2)

print(largest)