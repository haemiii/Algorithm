# from collections import deque
#
# def bfs_o(x, y):
#     queue = deque()
#     queue.append((x,y))
#
#     while queue:
#         x, y = queue.popleft()
#         v = picture[x][y]
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
#                 continue
#             if v == 'B':
#                 if picture[nx][ny] == v and not graph2[nx][ny]:
#                     queue.append((nx,ny))
#                     graph2[nx][ny] = True
#             else:
#                 if picture[nx][ny] != 'B' and not graph2[nx][ny]:
#                     queue.append((nx, ny))
#                     graph2[nx][ny] = True
#
# def bfs_x(x, y): # 적록색맹
#     queue = deque()
#     queue.append((x,y))
#
#     while queue:
#         x, y = queue.popleft()
#         v = picture[x][y]
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
#                 continue
#             if picture[nx][ny] == v and not graph1[nx][ny]:
#                 queue.append((nx, ny))
#                 graph1[nx][ny] = True
#
#
# n = int(input())
# picture = [list(input()) for _ in range(n)]
# graph1 = [[False]*n for _ in range(n)]
# graph2 = [[False]*n for _ in range(n)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]
# cnt1 = 0
# cnt2 = 0
#
# for i in range(n):
#     for j in range(n):
#         if not graph1[i][j]:
#             bfs_x(i, j)
#             cnt1 += 1
#         if not graph2[i][j]:
#             bfs_o(i, j)
#             cnt2 += 1
# print(cnt1, cnt2)
#
from collections import deque

def bfs_x(x, y, graph): # 적록색맹
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        v = picture[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if picture[nx][ny] == v and not graph[nx][ny]:
                queue.append((nx, ny))
                graph[nx][ny] = True


n = int(input())
picture = [list(input()) for _ in range(n)]
graph1 = [[False]*n for _ in range(n)]
graph2 = [[False]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
cnt1 = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if not graph1[i][j]:
            bfs_x(i, j, graph1)
            cnt1 += 1
        if picture[i][j] == 'G':
            picture[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not graph2[i][j]:
            bfs_x(i, j, graph2)
            cnt2 += 1

print(cnt1, cnt2)



