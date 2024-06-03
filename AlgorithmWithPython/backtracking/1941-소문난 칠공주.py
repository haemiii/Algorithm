# 7명의 여학생
# 자리는 가로나 세로로 반드시 인접
# 이다솜파 + 임도연파
# 이다솜파가 4명이상 존재! (임도연파는 3명까지!)

# 조건에 부합하는 모든 조합찾기 : 백트래킹
# 다 연결되어있는지 확인 : bfs

from collections import deque

graph = [list(input()) for _ in range(5)]
visited = [[False]*5 for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = []
cnt = 0

# 0, 3 -> 0, 4
# 0, 4 -> 1, 0
# 1. 조합찾기
def backtracking(start, s_count, y_count):
    global cnt
    if s_count + y_count == 7:
        if s_count >= 4 and bfs():
            cnt += 1
        return


    for i in range(start, 25):
        x, y = i // 5, i % 5
        if not visited[x][y]:
            visited[x][y] = True
            if graph[x][y] == 'S':
                backtracking(i+1, s_count+1, y_count)
            else:
                backtracking(i+1, s_count, y_count+1)
            visited[x][y] = False

def bfs():
    queue = deque()
    visited_bfs = [[0]*5 for _ in range(5)]
    start_x,  start_y = -1, -1

    for i in range(5):
        for j in range(5):
            if visited[i][j]:
                start_x, start_y = i, j
                break
        if start_x != -1:
            break
    queue.append((start_x, start_y))
    visited_bfs[start_x][start_y] = 1
    link = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= 5 or ny <= -1 or ny >= 5:
                continue
            if visited[nx][ny] and visited_bfs[nx][ny] == 0:
                queue.append((nx, ny))
                visited_bfs[nx][ny] = visited_bfs[x][y] + 1
                link += 1

    return link == 7

backtracking(0, 0, 0)
print(cnt)