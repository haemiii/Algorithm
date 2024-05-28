'''
팀 구성 : 모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택해야한다! -> 자신도 선택 가능!
어느팀에도 속하지 않는 학생들의 수를 계산하는 프로그램 작성

예시를 살펴보자!
(o) : x에서 시작해서 x로 돌아오는 순환구조!! : bfs(연결된 모든부분을 순환!)
3->3
4->7 , 7->6, 6->4

(x)
1->3
2->1
5->3
'''

import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,v):
    queue = deque()
    queue.append((i, v))
    visited[i]= True
    path = []
    while queue:
        i, v = queue.popleft()
        next_node = v - 1
        path.append(i)
        if visited[next_node]:
            if next_node in path:
                node_index = path.index(next_node)
                return len(path) - node_index
            return 0
        else:
            visited[next_node] = True
            queue.append((next_node, std[next_node]))

    return 0


t = int(input())
for i in range(t):
    cnt = 0

    n = int(input())
    std = list(map(int, input().split()))
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            cnt += bfs(i, std[i])
    print(n-cnt)