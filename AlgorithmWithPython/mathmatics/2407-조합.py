# N, M = map(int ,input().split())
#
# multiple = 1
# multiple2 = 1
#
# for i in range(N, N-M, -1):
#     multiple *= i
# for j in range(1, M+1):
#     multiple2 *= j
#
# print(multiple // multiple2)


### ! : 팩토리얼 이용

'''
fac(6) ->
    6 * fac(5) ->
        5 *fac(4) ->
            4 * fac(3) ->
                3 * fac(2) ->
                    2 *fac(1)
'''
n, m = map(int, input().split())

# 1
def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)
print(fac(6))

# 2
def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(fact(n)//(fact(n-m)*fact(m)))


