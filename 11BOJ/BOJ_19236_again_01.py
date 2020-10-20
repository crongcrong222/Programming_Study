dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
n = 4

myMap = [[None] * n for i in range(n)]
for i in range(n):
    tt = list(map(int,input().split()))
    for j in range(n):
        myMap[i][j] = [tt[j*2],tt[j*2+1]-1]
result = 0

def ban_sigae(direction):
    return (direction + 1) % 8




def find_fish_position(myMap,idx):
    for i in range(n):
        for j in range(n):
            if(myMap[i][j][0] == idx):
                return [i,j]
    return None


def move_fish(myMap,sang_x,sang_y):
    for kkkk in range(1,17):
        fish_position = find_fish_position(myMap,kkkk)
        if(fish_position != None):
            x, y = fish_position[0],fish_position[1]
            direction = myMap[x][y][1]
            for i in range(8):
                cx = x + dx[direction]
                cy = y + dy[direction]
                if cx>=0 and cx<4 and cy>=0 and cy<4:

                    if not(sang_x == cx and sang_y == cy):
                        myMap[x][y][1] = direction
                        myMap[cx][cy], myMap[x][y] = myMap[x][y], myMap[cx][cy]
                        break
                #두 경우가 모두 아니면 반시계 방향 갱신
                direction = ban_sigae(direction)


def can_eat_list(myMap,sang_x,sang_y):
    can_list = []
    direction = myMap[sang_x][sang_y][1]

    for i in range(4):
        sang_x += dx[direction]
        sang_y += dy[direction]
        #한 쪽 방향으로 쭉 찾기
        if sang_x>=0 and sang_y>=0 and sang_x<n and sang_y<n:
            if(myMap[sang_x][sang_y][0]!=-1):
                can_list.append([sang_x,sang_y])

    return can_list

import copy
def dfs(myMap,sang_x,sang_y,fish_sum):
    global result
    myMap = copy.deepcopy(myMap)
    fish_sum += myMap[sang_x][sang_y][0]
    myMap[sang_x][sang_y][0] = -1
    move_fish(myMap,sang_x,sang_y)
    can_list = can_eat_list(myMap,sang_x,sang_y)
    if(len(can_list) ==0):
        result = max(result,fish_sum)
        return
    for next_sang_x, next_sang_y in can_list:
        dfs(myMap,next_sang_x,next_sang_y,fish_sum)


dfs(myMap,0,0,0)
print(result)








