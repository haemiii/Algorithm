# 1번 풀이
# n = int(input())
# d = [[0]*3 for _ in range(n+1)]
# s = [int(input()) for _ in range(n)]
#
# if n == 1:
#     print(s[0])
# else:
#     d[1][1], d[1][2] = s[0], 0
#     d[2][1], d[2][2] = s[1], s[0] + s[1]
#
#     for i in range(3, n+1):
#         d[i][1] = max(d[i-2][1], d[i-2][2]) +s[i-1]
#         d[i][2] = d[i-1][1] + s[i-1]
#
#     print(max(d[n][1], d[n][2]))


# d[1] = 10
# d[2] = 20
# d[3] = 15
# d[4] = d[1] + s[4]
# d[k] = min(d[k-2], d[k-3]) + s[k]
# 2번 풀이
n = int(input())
d = [0]*(n+1)
s = [int(input()) for _ in range(n)]

if n == 1:
    print(s[0])
else:
    d[1] = s[0]
    d[2] = s[1]
    d[3] = s[2]
    for i in range(4, n+1):
        d[i] = min(d[i-2], d[i-3]) + s[i-1]

    print(sum(s) - min(d[n-1], d[n-2]))
