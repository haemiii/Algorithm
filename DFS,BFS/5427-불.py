from collections import deque

def fire_bfs(queue, graph):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= h or ny <= -1 or ny >= w:
                continue
            if location[nx][ny] == '.' or location[nx][ny] == '@':
                if graph[nx][ny] == -1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

def person_bfs(queue, graph):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= h or ny <= -1 or ny >= w:
                return graph[x][y] + 1
            if location[nx][ny] == '.' and graph[nx][ny] == -1:
                if fire_graph[nx][ny] > graph[x][y] + 1 or fire_graph[nx][ny] == -1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    return False

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(t):
    w, h = map(int, input().split())
    location = [list(input()) for _ in range(h)]

    fire = deque()
    fire_graph = [[-1]*w for _ in range(h)]
    person = deque()
    person_graph = [[-1]*w for _ in range(h)]

    for x in range(h):
        for y in range(w):
            if location[x][y] == '@':
                person.append((x, y))
                person_graph[x][y] = 0
            if location[x][y] == '*':
                fire.append((x, y))
                fire_graph[x][y] = 0



    fire_bfs(fire, fire_graph)
    return_value = person_bfs(person, person_graph)
    if not return_value:
        print("IMPOSSIBLE")
    else:
        print(return_value)

    for i in fire_graph:
        print(i)
    for j in person_graph:
        print(j)


