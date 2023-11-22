# GCD : the greatest common denominator(최대공약수)

'''
def gcd(x, y):
     if x == 0 or y == 0:
         return x + y
     if x > y:
         return gcd(x % y, y)
     else:
         return gcd(x, y % x)
'''
# LCM : the least common multiple(최소공배수)
'''multiple = (N*M) // x'''

'''시간초과!!!'''

# N, M = map(int, input().split())
#
# def gcd(x, y):
#     if x == 0 or y == 0:
#         return x + y
#     if x > y:
#         return gcd(x % y, y)
#     else:
#         return gcd(x, y % x)
#
#
# def lcm(x, y):
#     n = gcd(x, y)
#     i = 1
#     lcm = 0
#     while True:
#         lcm = n * i
#         if lcm % x == 0 and lcm % y == 0:
#             break
#         i += 1
#     return lcm
#
#
# print(gcd(N, M))
# print(lcm(N, M))



###

# N, M = map(int, input().split())
#
# def gcd(x, y):
#     if x == 0 or y == 0:
#         return x + y
#     if x > y:
#         return gcd(x % y, y)
#     else:
#         return gcd(x, y % x)
#
# x = gcd(N, M)
# multiple = (N*M) // x
#
# print(x)
# print(multiple)