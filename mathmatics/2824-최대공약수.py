# gcd 문제


'''
1000012028
 000012028
'''

### 재귀 호출 횟수 초과 문제 발생!

# def gcd(x, y):
#     if x == 0 or y == 0:
#         return x+y
#     if x > y:
#         return gcd(x%y , y)
#     else:
#         return gcd(x, y%x)
#
# multiple1 = 1
# multiple2 = 1
#
# N = int(input())
# A = list(map(int, input().split()))
# for i in A:
#     multiple1 *= i
#
# M = int(input())
# B = list(map(int, input().split()))
#
# for j in B:
#     multiple2 *= j
#
# g = gcd(multiple1, multiple2)
# g = str(g)
# if len(g) > 9:
#     g = g[len(g)-9:]
#     print(g)
# else:
#     print(g)


##
def gcd(a, b):
    while b>0:
        a, b = b, a%b
        return a

multiple1 = 1
multiple2 = 1

N = int(input())
A = list(map(int, input().split()))
for i in A:
    multiple1 *= i

M = int(input())
B = list(map(int, input().split()))

for j in B:
    multiple2 *= j

g = gcd(multiple1, multiple2)
g = str(g)
if len(g) > 9:
    g = g[len(g)-9:]
    print(g)
else:
    print(g)