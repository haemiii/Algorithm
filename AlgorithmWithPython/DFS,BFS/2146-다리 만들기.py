import sys
from collections import deque
input = sys.stdin.readline


def label_islands():
    island_id = 2
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                bfs_label(i, j, island_id)
                island_id += 1

def bfs_label(x, y, island_id):
    queue = deque([(x, y)])
    graph[x][y] = island_id
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = island_id
                queue.append((nx, ny))


def find_shortest_bridge():
    min_distance = sys.maxsize
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 1:
                distance = make_bridge(i, j, graph[i][j])
                if distance:
                    min_distance = min(min_distance, distance)
    return min_distance


def make_bridge(x, y, island_id):
    visited = [[False]*n for _ in range(n)]
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True

    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == 0:
                    queue.append((nx, ny, dist + 1))
                elif graph[nx][ny] > 1 and graph[nx][ny] != island_id:
                    return dist
    return None

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
bridge = [[0]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

label_islands()

shortest_length = find_shortest_bridge()
print(shortest_length)