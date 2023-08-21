# 1. k번째 약수
'''
    n : 자연수
    k : k번째로 작은 수
'''
# # n, k = input().split()
# n, k = map(int, input().split())
#
# cnt = 0
#
# for i in range(1, n+1):
#     if n%i == 0:
#         cnt +=1
#     if k == cnt:
#         print(k)
#         break
# else: # break를 안당했다 -> k 값이 더 크다
#     print(-1)



# 2. k번째 수
# import sys
#
# T = int(sys.stdin.readline())
# for i in range(T):
#     n, s, e, k = map(int, sys.stdin.readline().split())
#     array = list(map(int, sys.stdin.readline().split()))
#
#     array = array[s-1:e]
#     array.sort()
#     print(f"#{i+1}" ,array[k-1])

# 3. k번째 큰 수

# N, K = map(int, input().split())
# card = list(map(int, input().split()))
# sum = set()
#
# for i in range(0, N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             sum.add(card[i] + card[j] + card[k])
#
# sum = list(sum)
# sum.sort(reverse=True)
# print(sum[K-1])

# 4. 대표값

# import sys
#
# N = int(input())
# array = list(map(int, sys.stdin.readline().split()))
#
# # round는 round_half_even 방식을 택한다. -> 5.5 : 6 , 4.5 : 4
# ave = sum(array) / N
# ave = int(ave+0.5)  # 강제 내림!
#
# print(ave)
# min = 100
# index = 0
#
# for i, j in enumerate(array):
#     if abs(ave - j) < min:
#         sub = ave - j
#         index = i
#     elif abs(ave - j) == min:
#         if array[index] < array[i]:
#             index = i
# print(array[index], index+1)


# 5. 정다면체

'''
    4 : 1 ~ 4                 4 :  1 ~ 4
    6 : 1 ~ 6                20 :  1 ~ 20
    
    합 : 2 ~ 7     2 ~ 5           2 ~ 21
    합 : 3 ~ 8     3 ~ 6           3 ~ 22
    합 : 4 ~ 9     4 ~ 7
    합 : 5 ~ 10    5 ~ 8
    -----------   --------
        5 ~ 7    
        첫번째 주사위의 가장 큰 숫자 + 두번째 주사위의 가장 작은 숫자 
                            ~~~~~~~~
        첫번째 주사위의 가장 작은 숫자 + 두번째 주사위의 가장 큰 숫자
        
'''
# N, M = map(int ,input().split())
#
# if N < M:
#     for i in range(N + 1, (1+M)+1):
#         print(i, end=" ")
# elif N > M:
#     for i in range(M + 1, (1 + N) + 1):
#         print(i, end=" ")
# else:
#     print(N + 1)


# 6. 자릿수의 합

## 방법 1.

# N = int(input())
# num = list(input().split())

# def digit_sum(x):
#     plus = 0
#     for i in x:
#         plus += int(i)
#     return plus
#
# max = 0
# index = 0
# for i in range(N):
#     plus = digit_sum(num[i])
#     if max < plus:
#         max = plus
#         index = i
# print(num[index])


## 방법 2.
# def digit_sum(x):
#     sum = 0
#     while x > 0:
#         sum += x % 10
#         x //= 10
#     return sum
#
# max = 0
# for i in num:
#     total = digit_sum(i)
#     if total > max:
#         max = total
#         res = i
#
# print(res)


# 7. 소수 구하기


## 에라토스테네스 체
# x = 200000
# array = [True for _ in range(x+1)]
#
# for i in range(2, int((x ** 0.5)) + 1):
#     if array[i] == True:
#         j = 2
#         while i * j <= x:
#             array[i*j] = False
#             j += 1
#
#
# N = int(input())
# cnt = 0
# for i in range(2, N + 1):
#     if array[i] == True:
#         print(i)
#         cnt += 1
# print(cnt)

# 8. 뒤집은 소수
# n = 100000
# array = [True for _ in range(n+1)]
# for i in range(2, int(n ** 0.5) + 1):
#     if array[i] == True:
#         j = 2
#         while i * j <= n:
#             array[i * j] = False
#             j += 1
#
# def isPrime(x):
#     if x == 1:
#         return False
#     elif array[x] == True:
#         return True
#     else:
#         return False
#
# def reverse(x):
#     res = 0
#     while x > 0:
#         t = x % 10
#         res = res * 10 + t
#         x //= 10
#     return res
#
# N = int(input())
# num = list(map(int, input().split()))
# for i in num:
#     x = reverse(i)
#     if isPrime(x):
#         print(x, end=" ")

# 9. 주사위 게임
# import sys
# N = int(input())
# price = list()
# max = 0
# for i in range(N):
#     num = sys.stdin.readline().split()
#     num.sort()
#     a, b, c = map(int, num)
#     cnt = 0
#
#     if a== b and b == c:
#         money =10000 + a * 1000
#     elif a == b or  a == c:
#         money = 1000 + a * 100
#     elif b == c:
#         money = 1000 + b * 100
#     else:
#         money = c*100
#
#     if money > max:
#         max = money
#
# print(max)

# 10. 점수 계산
# N = int(input())
# answer = list(map(int, input().split()))
# score = [0 for _ in range(N)]
# sum = 0
#
# for idx, j in enumerate(answer):
#     if idx == 0:
#         if j == 0:
#             score[idx] = 0
#         else:
#             score[idx] = 1
#             sum += 1
#     else:
#         if j == 0:
#             score[idx] = 0
#         else:
#             if score[idx -1] > 0:
#                 score[idx] = score[idx -1] + 1
#             else:
#                 score[idx] = 1
#             sum += score[idx]
#
# print(sum)

## 다른 방법
N = int(input())
answer = list(map(int, input().split()))
sum = 0
cnt = 0

for x in answer:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0