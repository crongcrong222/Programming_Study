from collections import deque
'''
3
0 0 0
0 0 0
0 9 0
'''

'''

INF = 1e9

n = int(input())
myMap = [list(map(int,input().split())) for i in range(n)]
sang_size = 2

sang_position = [[i,j] for i in range(n) for j in range(n) if myMap[i][j] == 9]
sx, sy = sang_position[0]

dx = [-1,0,1,0]
dy = [0,1,0,-1]



q = deque()

def bfs():
    dist = [[-1] * n for i in range(n)]
    q.append([sx,sy])
    dist[sx][sy] = 0

    while(q):
        x,y = q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if(cx>=n or cy>=n or cx<0 or cy<0):
                continue
            if(dist[cx][cy] == -1 and myMap[cx][cy] <= sang_size):
                dist[cx][cy] = dist[x][y] + 1
                q.append([cx,cy])
    return dist

def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if(dist[i][j] != -1 and 1<= myMap[i][j] and myMap[i][j] < sang_size):
                if(dist[i][j] < min_dist):
                    min_dist = dist[i][j]
    if(min_dist == INF):
        return None
    else:
        return x,y,min_dist


result = 0
ate = 0

while(1):
    value = find(bfs())
    if value == None:
        print(result)
        break

    else:
        cx, cy = value[0], value[1]
        result += value[2]
        myMap[cx][cy] = 0
        ate += 1
        if(ate >= sang_size):
            sang_size += 1
            ate = 0


'''
INF = 1e9

n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]

sang_size = 2

sang_position = [[i, j] for i in range(n) for j in range(n) if arr[i][j] == 9]
sx, sy = sang_position[0]
arr[sx][sy] = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

#모든 위치까지의 최단!거리만! 계산하는 bfs함수

q = deque()
def bfs():
    #값이 -1이면 도달할 수 없다는 의미
    dist = [[-1] * n for i in range(n)]
    #시작위치는 도달가능하니까 0으로 바꿈
    q.append([sx,sy])
    dist[sx][sy] = 0

    while(q):
        x,y = q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if(cx<n and cx>=0 and cy<n and cy>=0):
                #자신의 크기 보다 작거나 같은 경우에 지나갈 수 있다
                if(dist[cx][cy] == -1 and arr[cx][cy] <=sang_size):
                    dist[cx][cy] = dist[x][y] + 1
                    q.append([cx,cy])
    return dist

#최단거리 테이블이 주어졌을 때, 먹을 수 있는 물고기를 찾는 함수
def find(dist):
    x, y = 0, 0
    min_dis = INF
    for i in range(n):
        for j in range(n):
            #도달 가능하면서 먹을 수 있는 물고기이면
            if(dist[i][j] != -1 and 1 <= arr[i][j] and arr[i][j] < sang_size):
                if dist[i][j] < min_dis:
                    x,y = i,j
                    min_dis = dist[i][j]
    if min_dis == INF:
        return None
    else:
        return x,y,min_dis

result = 0
ate = 0

while(1):
    value = find(bfs())

    if value == None:
        print(result)
        break
    else:
        cx,cy = value[0], value[1]
        result += value[2]
        arr[cx][cy] = 0
        ate += 1
        #자기 크기 이상으로 먹은 경우, 크기 증가
        if(ate >= sang_size):
            sang_size += 1
            ate = 0

