from _collections import deque
#https://jjangsungwon.tistory.com/27

def change(direction,di):
    if di == "L":
        return (direction + 1)%4
    else:
        return (direction - 1)%4
n = int(input())

dx = [0,-1,0,1]
dy = [1,0,-1,0]

myMap = [[0 for i in range(n)] for j in range(n)]

k = int(input())
for _ in range(k):
    sx,sy = map(int,input().split())
    myMap[sx-1][sy-1] = 1

l = int(input())

timedic = dict()
for i in range(l):
    ti,di = input().split()
    timedic[int(ti)] = di
time = 1
x,y = 0,0
visited = deque([[x,y]])
myMap[x][y] = 2
direction = 0
while(1):
    x = x + dx[direction]
    y = y + dy[direction]
    if(x<n and y<n and x>=0 and y>=0 and myMap[x][y] !=2):
        if myMap[x][y] != 1:
            tail_x,tail_y = visited.popleft()
            myMap[tail_x][tail_y] = 0
        myMap[x][y] =2
        visited.append([x,y])
        if( time in timedic.keys()):
            direction =change(direction,timedic[time])
        time+=1
    else:
        break
print(time)


