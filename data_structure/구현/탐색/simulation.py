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

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# largest = 0
#
#
# def find_max(largest, sum1, sum2):
#     if largest < sum1:
#         largest = sum1
#     if largest < sum2:
#         largest = sum2
#     return largest
#
#
# for i in range(N):
#     sum1= sum2 = 0
#     for j in range(N):
#         sum1 += board[i][j]
#         sum2 += board[j][i]
#     largest = find_max(largest, sum1, sum2)
#
# sum1 = sum2 = 0
#
# for i in range(N):
#     sum1 += board[i][i]
#     sum2 += board[i][N-i-1]
# largest = find_max(largest, sum1, sum2)
#
# print(largest)

# 7. 사과나무
'''
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19  
'''

# N = int(input())
# apple = [list(map(int, input().split())) for _ in range(N)]
# sum = 0
# s = e = N // 2
# for i in range(N):
#     for j in range(s, e + 1):
#         sum += apple[i][j]
#     if i < N//2:
#         s -= 1
#         e += 1
#     else:
#         s += 1
#         e -= 1
#
# print(sum)


# 8. 곳감(모래시계)

'''
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19  
3
2 0 3
5 1 2
3 1 4
'''

### 방법 1.

# N = int(input())
# array = [list(map(int, input().split())) for _ in range(N)]
#
# M = int(input())
# for i in range(M):
#     command = list(map(int, input().split()))
#     newArray = [0 for _ in range(N)]
#
#     if command[1] == 0:
#         for j in range(N):
#             newArray[(j + (5 - command[2])) % 5] = array[command[0]-1][j]
#     else:
#         for j in range(N):
#             newArray[(j + command[2]) % 5] = array[command[0]-1][j]
#
#     array[command[0]-1] = newArray[0:5]
# print(array)
#
# s = 0
# e = N
# sum = 0
# for i in range(N):
#     for j in range(s, e):
#         sum += array[i][j]
#     if i < N // 2:
#         s += 1
#         e -= 1
#     else:
#         s -= 1
#         e += 1
#
# print(sum)


### 방법 2.

# N = int(input())
# array = [list(map(int, input().split())) for _ in range(N)]
# M = int(input())
#
# for i in range(M):
#     h, t, k = map(int, input().split())
#     if t == 0:
#         for _ in range(k):
#             array[h - 1].append(array[h - 1].pop(0))
#     else:
#         for _ in range(k):
#             array[h - 1].insert(0, array[h - 1].pop())
#
# s = 0
# e = N
# sum = 0
# for i in range(N):
#     for j in range(s, e):
#         sum += array[i][j]
#     if i < N // 2:
#         s += 1
#         e -= 1
#     else:
#         s -= 1
#         e += 1
#
# print(sum)

# 9. 봉우리

'''
5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2

[a][b] -> [a][b+1]
       -> [a][b-1]
       -> [a-1][b]
       -> [a+1][b]

'''

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# N = int(input())
# array = [list(map(int, input().split())) for _ in range(N)]
# array.insert(0, [0]*N)
# array.append([0]*N)
# for x in array:
#     x.insert(0, 0)
#     x.append(0)
#
# cnt = 0
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if all(array[i][j] > array[i+dx[k]][j+dy[k]] for k in range(4)):
#             cnt += 1


# 10. 스도쿠 검사


'''
1 4 3 6 2 8 5 7 9 
5 7 2 1 3 9 4 6 8 
9 8 6 7 5 4 2 3 1  
3 9 1 5 4 2 7 8 6 
4 6 8 9 1 7 3 5 2 
7 2 5 8 6 3 9 1 4 
2 3 7 4 8 1 6 9 5 
6 1 9 2 7 5 8 4 3 
8 5 4 3 9 6 1 2 7

'''

# sudoku = [list(map(int, input().split())) for _ in range(9)]
#
# def check(a):
#     for i in range(9):
#         check_row = [0] * 10
#         check_column = [0] * 10
#
#         for j in range(9):
#             check_row[sudoku[i][j]] = 1
#             check_column[sudoku[j][i]] = 1
#         if sum(check_row) != 9 or sum(check_column) != 9:
#             return False
#     for i in range(3):
#         for j in range(3):
#             check_square = [0] * 10
#             for k in range(3):
#                 for s in range(3):
#                     check_square[sudoku[i*3+k][j*3+s]] = 1
#                 if sum(check_square) != 9:
#                     return False
#     return True
#
#
# if check(sudoku):
#     print("YES")
# else:
#     print("NO")


# 11. 격자판 회문수

'''
2 4 1 5 3 2 6 
3 5 1 8 7 1 7 
8 3 2 7 1 3 8 
6 1 2 3 2 1 1 
1 3 1 3 5 3 2 
1 1 2 5 6 5 2 
1 2 2 2 2 1 5
'''

# array = [list(map(int, input().split())) for _ in range(7)]
# sum = 0
#
# for i in range(7):
#     s = 0
#     e = 4
#     for j in range(3):
#         for k in range(2): # 0, 1
#             if array[i][s+k] != array[i][e-k]:
#                 break
#         else:
#             sum += 1
#         s += 1
#         e += 1
#
#     s = 0
#     e = 4
#     for j in range(3):
#         for k in range(2):  # 0, 1
#             if array[s+k][i] != array[e-k][i]:
#                 break
#         else:
#             sum += 1
#         s += 1
#         e += 1
#
#
# print(sum)


## 방법 2

board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if board[i+k][j] != board[i+4-k][j]:
                break
        else:
            cnt += 1

print(cnt)