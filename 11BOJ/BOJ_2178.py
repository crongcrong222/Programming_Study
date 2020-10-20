from collections import deque

n, m = map(int, input().split())

a = [list(map(int, input())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

q = deque()

sx, sy = 0, 0

q.append([sx, sy])

visited[sx][sy] = 1

dx = [-1,1,0,0]
dy = [0,0,1,-1]
while(len(q) != 0):
    x, y = map(int, q.popleft())
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if(cx>=n or cy >=m or cx<0 or cy<0):
            continue
        if(a[cx][cy] != 0 and not visited[cx][cy]):
            visited[cx][cy] = visited[x][y] + 1
            q.append([cx,cy])


print(visited[n-1][m-1])
