dy = [0,1,0,-1]
dx = [1,0,-1,0]



def dfs(idx,x,y,number):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    number += myMap[x][y]
    if(idx == 6):
        result.append(number)
        return
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if(cx>=4 or cy>=4 or cx<0 or cy<0):
            continue
        else:
            dfs(idx+1,cx,cy,number)
for t in range(1, int(input())+1):
    myMap = [list(map(str,input().split())) for _ in range(4)]
    result = []

    for i in range(4):
        for j in range(4):
            dfs(0,i,j,'')
    answer = set(result)
    print("#{} {}".format(t,len(answer)))