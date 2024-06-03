# 1924 : 2007년

"""
    2007년 1월 1일 : 월요일
"""
# x, y = map(int, input().split())
#
# days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
# year = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30 ,10 : 31, 11 : 30, 12 : 31}
#
# sum_days = 0
# for i in range(1, x):
#     sum_days += year[i]
# sum_days += y
#
# print(days[(sum_days % 7)-1])


##
# Day = 0
# x, y = map(int, input().split())
#
# days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
# calender = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# for i in range(x-1):
#     Day += calender[i]
# Day = (Day+y)% 7
# print(days[Day])

# 8393번 : 합

# N = int(input())
# sum = 0
#
# for i in range(1, N+1):
#     sum += i
#
# print(sum)


##
# N = int(input())
# print((N*(N+1)) // 2)

# 10818번 : 최소, 최대

# N = int(input())
# num_list = list(map(int, input().split()))
#
# print(min(num_list), max(num_list))


# 2438번 : 별 찍기

# N = int(input())
#
# for i in range(N):
#     for j in range(i+1):
#         print('*', end='')
#     print()


##

# N = int(input())
#
# for i in range(N):
#     print('*' * (i + 1))


# 2439번 : 별 찍기

# N = int(input())
#
# for i in range(1, N+1):
#     for j in range(N-i):
#         print(' ', end='')
#     for k in range(i):
#         print('*', end='')
#     print()


##
N = int(input())
for i in range(1, N+1):
    print(' ' * (N-i), end='')
    print('*' * i)

