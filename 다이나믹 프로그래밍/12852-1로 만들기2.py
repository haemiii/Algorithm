n = int(input())
d = [0]* (n+1)
pre = [0] * (n+1)
d[1] = 0
for i in range(2, n+1):
    d[i] = d[i-1] + 1
    pre[i] = i-1
    if i % 3 == 0:
        if d[i // 3] + 1 < d[i]:
            d[i] = d[i // 3] + 1
            pre[i] = i // 3

    # 2로 나누어 떨어지는 경우를 처리
    if i % 2 == 0:
        if d[i // 2] + 1 < d[i]:
            d[i] = d[i // 2] + 1
            pre[i] = i // 2

print(d[n])
path = []
while n > 0:
    path.append(n)
    n = pre[n]

print(' '.join(map(str, path)))