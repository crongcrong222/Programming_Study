

'''
6 2 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
5 4 1 1
1 1 3 5


6 5 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
3 3 3 5
6 5 3 5


14


6 3 13
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5

-1


6 3 100
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 1 0 0
0 0 0 1 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5

-1
'''
dx = [-1,1,0,0]
dy = [0,0,1,-1]

from queue import PriorityQueue
from collections import deque
import heapq

def son_cal_dist(son):
    ssx, ssy = son[1],son[2]
    endx,endy = son[3],son[4]
    q = deque([[ssx, ssy]])
    vvvv = [[0] * n for i in range(n)]
    dddd = [[-1] * n for i in range(n)]
    vvvv[ssx][ssy] = 1
    dddd[ssx][ssy] = 0
    while (q):
        x, y = q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if (cx >= n or cy >= n or cx < 0 or cy < 0):
                continue
            else:
                if (vvvv[cx][cy] == 0 and myMap[cx][cy] == 0):
                    dddd[cx][cy] = dddd[x][y] + 1
                    vvvv[cx][cy] = 1
                    q.append([cx, cy])
    for i in range(n):
        for j in range(n):
            print(dddd[i][j], end=' ')
        print()
    print('-----------')
    return dddd[endx][endy]

def cal_dist(sx,sy):
    q = deque([[sx,sy]])
    visit = [[0] * n for i in range(n)]
    visit[sx][sy] = 1
    dist[sx][sy] = 0
    while(q):
        x, y = q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if(cx>=n or cy>=n or cx<0 or cy<0):
                continue
            else:
                if(visit[cx][cy] == 0 and myMap[cx][cy] == 0):
                    dist[cx][cy] = dist[x][y] + 1
                    visit[cx][cy] = 1
                    q.append([cx,cy])

n, customer, energy = map(int, input().split())
myMap = [list(map(int, input().split())) for i in range(n)]
sx, sy = map(int, input().split())
sx = sx - 1
sy = sy - 1

dist = [[-1] * n for i in range(n)]
cus = [[0] for i in range(customer)]
cus_list = PriorityQueue()
cus_heap = []
for i in range(customer):
    visit =[[0] * n for i in range(n)]
    cus[i] = list(map(int,input().split()))
    cus[i] = [0, cus[i][0]-1,cus[i][1]-1,cus[i][2]-1,cus[i][3]-1 ]

cal_dist(sx,sy)
for i in range(customer):
    cus[i][0] = dist[cus[i][1]][cus[i][2]]
    print("son_cal_dist",son_cal_dist(cus[i]))
    cus[i].append(son_cal_dist(cus[i]))
print(cus)
heapq.heapify(cus)

answer = -1


for kk in range(customer):
    cal_dist(sx, sy)
    for i in range(n):
        for j in range(n):
            print(dist[i][j], end=' ')
        print()
    print()
    print("before",sx,sy)

    heapq.heapify(cus)
    sonnim = heapq.heappop(cus)
    print("select",sonnim)
    if(sonnim[0] == -1 or sonnim[-1] == -1):
        energy = -1
        print(111)
        break
    if(energy<=sonnim[0]):
        energy = -1
        print(222)
        break
    else:
        print("energy",energy)
        energy-=sonnim[0]
        print("get son and energy",energy)
        #손님있는 곳 까지 감
        sx,sy = sonnim[1],sonnim[2]
        son_dist = sonnim[-1]
        if(energy<son_dist):
            print(333)
            energy = -1
            break
        else:
            print("to dist",son_dist)
            energy-=son_dist
            print("after energy",energy)
            energy +=son_dist * 2
            print("charge",energy)
            sx,sy = sonnim[3],sonnim[4]
            print("afer",sx,sy)
            dist = [[-1] * n for i in range(n)]
            cal_dist(sx,sy)
            for kk in range(n):
                for jj in range(n):
                    print(dist[kk][jj], end=' ')
                print()
            print('after visit')
            for i in range(len(cus)):
                cus[i][0] = dist[cus[i][1]][cus[i][2]]
                print("i",i,"cusss",cus[i])

print(energy)


'''
dx = [-1,1,0,0]
dy = [0,0,1,-1]

from queue import PriorityQueue
from collections import deque
import heapq

def son_cal_dist(son):
    ssx, ssy = son[1],son[2]
    endx,endy = son[3],son[4]
    q = deque([[ssx, ssy]])
    vvvv = [[0] * n for i in range(n)]
    dddd = [[-1] * n for i in range(n)]
    vvvv[ssx][ssy] = 1
    dddd[ssx][ssy] = 0
    while (q):
        x, y = q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if (cx >= n or cy >= n or cx < 0 or cy < 0):
                continue
            else:
                if (vvvv[cx][cy] == 0 and myMap[cx][cy] == 0):
                    dddd[cx][cy] = dddd[x][y] + 1
                    vvvv[cx][cy] = 1
                    q.append([cx, cy])
    return dddd[endx][endy]

def cal_dist(sx,sy):
    q = deque([[sx,sy]])
    visit = [[0] * n for i in range(n)]
    visit[sx][sy] = 1
    dist[sx][sy] = 0
    while(q):
        x, y = q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if(cx>=n or cy>=n or cx<0 or cy<0):
                continue
            else:
                if(visit[cx][cy] == 0 and myMap[cx][cy] == 0):
                    dist[cx][cy] = dist[x][y] + 1
                    visit[cx][cy] = 1
                    q.append([cx,cy])

n, customer, energy = map(int, input().split())
myMap = [list(map(int, input().split())) for i in range(n)]
sx, sy = map(int, input().split())
sx = sx - 1
sy = sy - 1

dist = [[-1] * n for i in range(n)]
cus = [[0] for i in range(customer)]
cus_list = PriorityQueue()
cus_heap = []
for i in range(customer):
    visit =[[0] * n for i in range(n)]
    cus[i] = list(map(int,input().split()))
    cus[i] = [0, cus[i][0]-1,cus[i][1]-1,cus[i][2]-1,cus[i][3]-1 ]

cal_dist(sx,sy)
for i in range(customer):
    cus[i][0] = dist[cus[i][1]][cus[i][2]]
    cus[i].append(son_cal_dist(cus[i]))
heapq.heapify(cus)

for kk in range(customer):
    cal_dist(sx, sy)
    heapq.heapify(cus)
    sonnim = heapq.heappop(cus)
    if(sonnim[0] == -1 or sonnim[-1] == -1):
        energy = -1
        break
    if(energy<=sonnim[0]):
        energy = -1
        break
    else:
        energy-=sonnim[0]
        sx,sy = sonnim[1],sonnim[2]
        son_dist = sonnim[-1]
        if(energy<son_dist):
            energy = -1
            break
        else:
            energy-=son_dist
            energy +=son_dist * 2
            sx,sy = sonnim[3],sonnim[4]
            dist = [[-1] * n for i in range(n)]
            cal_dist(sx,sy)
            for i in range(len(cus)):
                cus[i][0] = dist[cus[i][1]][cus[i][2]]

print(energy)


'''