import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

    return True


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

t = int(input())
for i in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for j in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in graph:
        print(i)
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                bfs(x, y)
                cnt += 1


    print(cnt)

