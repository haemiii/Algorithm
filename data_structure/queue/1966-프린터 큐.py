import sys
x = int(input())

for i in range(x):
    N, M = map(int, input().split())
    loc = list(map(int, sys.stdin.readline().split()))

    for j in range(len(loc)):
