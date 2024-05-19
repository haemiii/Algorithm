import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, input().split())
tomato = []
for i in range(h):
    tomato.append([list(map(int, input().split())) for _ in range(n)])
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

queue = deque()
for i in range(h):
    for j in range(n):
        if tomato[i][j].count(1) != 0:
            for k in range(m):
                if tomato[i][j][k] == 1:
                    queue.append((i, j, k))
max_value = 0
while queue:
    z, x, y = queue.popleft()
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <= -1 or nx >= n or ny <= -1 or ny >= m or nz <= -1 or nz >= h:
            continue
        if tomato[nz][nx][ny] == 0 and not visited[nz][nx][ny]:
            tomato[nz][nx][ny] = tomato[z][x][y] + 1
            queue.append((nz, nx, ny))

for i in tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        max_value = max(max_value, max(j))

print(max_value-1)

