# 귀납적으로 생각
# n = 1, z로 탐색 가능
# n = k 일때 탐색 가능하다면
# n = k+1 -> k로 구역을 나눠서 탐색

# 0,0 / 0, 2 / 2, 0/ 2, 2

def z(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n-1)
    if r < half and c < half:
        return z(n-1, r, c)
    if r < half <= c:
        return half*half + z(n-1, r, c-half)
    if r >= half > c:
        return 2*half*half + z(n-1, r-half, c)
    else:
        return 3*half*half + z(n-1, r-half, c-half)

n, r, c = map(int, input().split())


print(z(n, r, c))