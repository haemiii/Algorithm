def backtracking(pointer):
    global max_value
    if pointer == n:
        cnt = sum(1 for i in range(n) if s[i] <= 0)
        max_value = max(cnt, max_value)
        return

    if s[pointer] <= 0:
        backtracking(pointer + 1)
        return

    broken = False
    for i in range(n):
        if i != pointer and s[i] > 0:
            broken = True
            s[pointer] -= w[i]
            s[i] -= w[pointer]
            backtracking(pointer + 1)
            s[pointer] += w[i]
            s[i] += w[pointer]

    if not broken:
        backtracking(pointer + 1)

n = int(input())
s = []
w = []
max_value = 0

for i in range(n):
    a, b = map(int, input().split())
    s.append(a)
    w.append(b)

backtracking(0)
print(max_value)
