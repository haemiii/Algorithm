import sys

n, c = map(int, sys.stdin.readline().rstrip().split())
house = [sys.stdin.readline().rstrip() for _ in range(n)]

house.sort()