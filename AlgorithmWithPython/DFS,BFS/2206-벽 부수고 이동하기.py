import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    # 큐 초기화
    queue = deque()
    queue.append((0, 0, 0))  # (x, y, 벽을 부순 횟수)
    visited[0][0][0] = 1  # (x, y, 벽을 부순 횟수)

    while queue:
        x, y, broken = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][broken]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    queue.append((nx, ny, broken))

                if graph[nx][ny] == 1 and broken == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][broken] + 1
                    queue.append((nx, ny, 1))

    return -1

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())
