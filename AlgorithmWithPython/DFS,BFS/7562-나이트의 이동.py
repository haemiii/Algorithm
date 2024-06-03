from collections import deque

dx = [1, 2, 1, 2, -1, -2, -1, -2]
dy = [2, 1, -2, -1, 2, 1, -2, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if graph[nx][ny] == -1:
                return graph[x][y] + 1
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


t = int(input())

for i in range(t):
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    graph[a][b] = -1

    if x == a and y == b:
        print(0)
    else:
        value = bfs(x, y)
        print(value)







