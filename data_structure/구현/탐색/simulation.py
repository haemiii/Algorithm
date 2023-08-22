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


a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split()) # 구간
    for i in range((e-s+1)//2):  # 횟수
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(x, end=" ")