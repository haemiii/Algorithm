from itertools import combinations

while True:
    num = list(map(int, input().split()))
    if num[0] == 0:
        break

    for comb in combinations(num[1:], 6):
        print(' '.join(map(str, comb)))


