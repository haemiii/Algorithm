# k번을 말처럼 행동할 수 있다..
# 말 + 원숭이 행동의 순서가 중요하다.

import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    queue = deque([(0, 0, 0, 0)])
    visited = [[[False]*(k + 1) for _ in range(w)] for _ in range(h)]
    visited[0][0][0] = True

    while queue:
        x, y, dist, cnt = queue.popleft()

        if x == h-1 and y == w-1:
            return dist

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 0 and not visited[nx][ny][cnt]:
                    visited[nx][ny][cnt] = True
                    queue.append((nx, ny, dist+1, cnt))
        if cnt < k:
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if graph[nx][ny] == 0 and not visited[nx][ny][cnt+1]:
                        visited[nx][ny][cnt+1] = True
                        queue.append((nx, ny, dist+1, cnt+1))

    return -1

k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

hx = [1, 1, 2, 2, -1, -1, -2, -2]
hy = [2, -2, 1, -1, 2, -2, 1, -1]

print(bfs())