from collections import deque, defaultdict


def bfs(graph,start,visited):
    q = deque([start])
    visited[start] = 1

    while q:
        tmp = q.popleft()
        print(tmp, end=' ')
        for i in graph[tmp]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
n,m,start = map(int,input().split())

visited = [0 for i in range(m + 1)]
graph = defaultdict(set)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].add(b)

bfs(graph,start,visited)