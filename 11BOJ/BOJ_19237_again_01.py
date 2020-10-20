'''

5 3 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3

'''
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n, sang_num, smell_time = map(int,input().split())
myMap = [list(map(int,input().split())) for i in range(n)]
now_direction = list(map(int,input().split()))
priority = [[list(map(int,input().split())) for i in range(4)] for j in range(sang_num)]
smell = [[[0,0]] * n for i in range(n)]
def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            #만약 해당 위치에 상어가 있으면 냄새 업데이트하기
            if myMap[i][j] != 0 :
                smell[i][j] = [myMap[i][j],smell_time]

def move_sang():
    #이동하고 나서 이전 결과 값(상어 번호)를 비교하기 위한 새로운 map 리스트 만들기
    nowMap = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            #만약 해당 위치에 상어가 있으면 상어 움직이게 하기
            if(myMap[i][j] != 0):
                #움직일 방향을 상어 번호의 방향 우선순위에 따라 결정하기
                moving_direction = now_direction[myMap[i][j]-1]
                #냄새가 존재하는 곳인지 아닌지 나눈다
                #이를 위해 flag를 둔다
                smellNo = False
                #각 방향을 확인하자
                for dir in range(4):
                    cx = i + dx[priority[myMap[i][j]-1][moving_direction-1][dir]-1]
                    cy = j + dy[priority[myMap[i][j]-1][moving_direction-1][dir]-1]
                    if cx>=n or cy>=n or cx<0 or cy<0 :
                        continue
                    else:
                        if smell[cx][cy][1] == 0:
                            #냄새가 없으면,
                            smellNo = True
                            #이동을 하는데 이동 전 이동할 방향을 선정하여 now_direction에 업데이트하기
                            now_direction[myMap[i][j]-1] = priority[myMap[i][j]-1][moving_direction-1][dir]

                            #해당 상어 아무 것도 없으면 이동 시키기
                            if nowMap[cx][cy] == 0:
                                nowMap[cx][cy] = myMap[i][j]
                            else:
                                nowMap[cx][cy] = min(nowMap[cx][cy], myMap[i][j])
                            break
                if smellNo :
                    #냄새가 존재하지 않으므로
                    continue
                #냄새가 존재하면 해당되는 곳으로 이동하기
                for dir in range(4):
                    cx = i + dx[priority[myMap[i][j]-1][moving_direction-1][dir]-1]
                    cy = j + dy[priority[myMap[i][j]-1][moving_direction-1][dir]-1]
                    if cx>=n or cy>=n or cx<0 or cy<0:
                        continue
                    else:
                        #만약에 자신의 냄새가 있는 곳이면
                        if smell[cx][cy][0] == myMap[i][j]:
                            #이동을 하면서 이동 방향 업데이트
                            now_direction[myMap[i][j] - 1] = priority[myMap[i][j] - 1][moving_direction - 1][dir]
                            #상어 이동
                            nowMap[cx][cy] = myMap[i][j]
                            break
    return nowMap



time = 0

while(1):

    update_smell()
    tmp = move_sang()
    myMap = tmp
    time += 1
    finish = True
    for i in range(n):
        for j in range(n):
            if(myMap[i][j]>1):
                finish = False
    if finish:
        print(time)
        break
    if time>=1000:
        print("time",time,-1)
        break