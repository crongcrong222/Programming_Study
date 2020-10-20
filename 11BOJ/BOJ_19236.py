import copy
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
n=4
# 4 X 4 크기 격자에 존재하는 각 물고기의 번호(없으면 -1)와 방향 값을 담는 테이블


myMap = [[None] * n for i in range(n)]
for i in range(n):
    tt = list(map(int,input().split()))
    for j in range(n):
        myMap[i][j] = [tt[j*2],tt[j*2+1]-1]
result = 0
# 8가지 방향에 대한 정의


# 현재 위치에서 왼쪽으로 회전된 결과 반환
def ban_sigae(direction):
    return (direction + 1) % 8



# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish_position(myMap,idx):
    for i in range(n):
        for j in range(n):
            if(myMap[i][j][0] == idx):
                return [i,j]
    return None

# 모든 물고기를 회전 및 이동시키는 함수
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

# 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
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

# 모든 경우를 탐색하기 위한 DFS 함수
def dfs(myMap,sang_x,sang_y,fish_sum):
    global result
    myMap = copy.deepcopy(myMap)
    fish_sum += myMap[sang_x][sang_y][0]
    myMap[sang_x][sang_y][0] = -1
    move_fish(myMap,sang_x,sang_y)
    can_list = can_eat_list(myMap,sang_x,sang_y)
    print(can_list)
    if(len(can_list) ==0):
        result = max(result,fish_sum)
        return
    for next_sang_x, next_sang_y in can_list:
        dfs(myMap,next_sang_x,next_sang_y,fish_sum)

# 청소년 상어의 시작 위치(0, 0)에서부터 재귀적으로 모든 경우 탐색
dfs(myMap,0,0,0)
print(result)