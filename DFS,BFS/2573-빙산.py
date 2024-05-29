'''
입력값

5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
'''
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melt_ice():
    new_ice = [row[:] for row in ice]
    for x in range(1, n-1):
        for y in range(1, m-1):
            if ice[x][y] > 0:
                water_count = sum(ice[x+dx[k]][y+dy[k]] == 0 for k in range(4))
                new_ice[x][y] = max(0, ice[x][y] - water_count)
    return new_ice


def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 1 <= nx < n-1 and 1 <= ny < m-1:
                if not visited[nx][ny] and ice[nx][ny] > 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


def count_icebergs():
    visited = [[False]*m for _ in range(n)]
    count = 0
    for x in range(1, n-1):
        for y in range(1, m-1):
            if ice[x][y] > 0 and not visited[x][y]:
                bfs(x, y, visited)
                count += 1
    return count


year = 0
while True:
    ice = melt_ice()
    year += 1
    iceberg_count = count_icebergs()
    if iceberg_count == 0:
        print(0)
        break
    if iceberg_count > 1:
        print(iceberg_count)
        print(year)
        break
