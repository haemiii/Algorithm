import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, k):
    max_pos = 100000
    visited = [-1] * (max_pos + 1)
    visited[x] = 0

    queue = deque([x])
    while queue:
        x = queue.popleft()

        if x == k:
            return visited[x]
        if 2*x <= max_pos and visited[2*x] == -1:
            visited[2*x] = visited[x]
            queue.append(2*x)
        if 0 <= x-1 and (visited[x-1] == -1 or visited[x-1] > visited[x] + 1):
            visited[x-1] = visited[x] + 1
            queue.append(x-1)
        if x+1 <= max_pos and (visited[x+1] == -1 or visited[x+1] > visited[x] + 1):
            visited[x+1] = visited[x] + 1
            queue.append(x+1)


n, k = map(int, input().strip().split())
print(bfs(n,k))