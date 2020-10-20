def bfs(n,sx,sy,myMap,visit,danji):

    queue = [[sx,sy]]
    cnt = 1
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    while(queue):
        x,y = queue.pop(0)
        visit[x][y] = danji
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if(cx<0 or cy<0 or cx >=n or cy >=n):
                continue
            else:
                if(myMap[cx][cy] == 1 and visit[cx][cy] == 0):
                    visit[cx][cy] = danji
                    queue.append([cx,cy])
                    cnt +=1

    return visit,cnt

n = int(input())

myMap = []

for i in range(n):
    myMap.append(list(map(int,input())))

visit=[[0 for i in range(n)]for j in range(n)]

danji = 0
list_danji = []
for i in range(n):
    for j in range(n):
        if(myMap[i][j] == 1 and visit[i][j] == 0):
            danji +=1
            visit,cnt = bfs(n,i,j,myMap,visit,danji)
            list_danji.append(cnt)

list_danji.sort()
print(len(list_danji))
for i in range(len(list_danji)):
    print(list_danji[i])
