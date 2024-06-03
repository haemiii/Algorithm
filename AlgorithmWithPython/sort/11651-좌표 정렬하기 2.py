import sys
input = sys.stdin.readline

n = int(input())
location = [list(map(int, input().split())) for _ in range(n)]
location = sorted(location, key=lambda x :(x[1], x[0]))

for i in location:
    print(' '.join(map(str, i)))

