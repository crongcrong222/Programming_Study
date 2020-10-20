
#1. 벽 선택 3개 하기
#2. 바이러스 퍼지게 하기
#3. 안전 영역 계산
#4. 위를 반복해서 안전영역가장 큰거 도출

n,m = map(int,input().split())

myMap = [list(map(int,input().split())) for i in range(n)]
import copy

dx=[-1,1,0,0]
dy=[0,0,1,-1]
vaList =[]
for i in range(n):
    for j in range(m):
        if myMap[i][j] == 2:
            vaList.append([i,j])

answer = 0

def go_virus(vx,vy,tmpMAp):
    if tmpMAp[vx][vy] == 2:
        for d in range(4):
            cx = vx + dx[d]
            cy = vy + dy[d]
            if cx>=0 and cy >=0 and cx<n and cy<m:
                if tmpMAp[cx][cy] == 0:
                    tmpMAp[cx][cy] = 2
                    go_virus(cx,cy,tmpMAp)



def select_wall(fromPosition,cnt):
    global answer
    if cnt == 3:
        tmpMap = copy.deepcopy(myMap)
        for vaNum in vaList:
            vx, vy = vaNum
            go_virus(vx,vy,tmpMap)
        candisum =sum( jj.count(0) for jj in tmpMap)
        answer = max(answer,candisum)
        return True
    else:
        for i in range(fromPosition,n*m):
            x = i//m
            y = i% m
            if(myMap[x][y]==0):
                myMap[x][y] = 1
                select_wall(i,cnt+1)
                myMap[x][y] = 0


select_wall(0,0)

print(answer)