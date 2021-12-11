n, m = map(int,input().split())
myMap = [list(map(int,input()))for i in range(n)]

visited = [[0] * m for i in range(n)]


dx = [-1,0,0,1]
dy = [0,1,-1,0]

from collections import deque
def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m :
                if myMap[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx,ny])
    return visited[n-1][m-1]

print(bfs(0,0))
