''' input
4 4 2 1
1 2
1 3
2 3
2 4
'''

# dfs이용
# 최단거리 K구하기!

# city = []
# def dfs(x, cnt): #현재 위치
#
#     for i in graph[x]:
#         if cnt+1 == k:
#             city.append(i)
#         dfs(i, cnt+1)
#
#
#
# n, m, k, x = map(int, input().split())
# graph = [[] for i in range(n+1)]
#
# for i in range(m):
#     x = list(map(int, input().split()))
#     graph[x[0]].append(x[1])
#
# dfs(1, 0)
#
# if len(city) == 0:
#     print(-1)
# else:
#     for i in city:
#         print(i)


# bfs : 모든 간선의 비용이 동일할때는 bfs를 통해서 최단거리를 찾을 수 있다.
# 시간복잡도 : O(N+M)

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
print(graph)
distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)






