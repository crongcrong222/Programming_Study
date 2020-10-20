#https://www.acmicpc.net/problem/17135

n,m,d = map(int,input().split())
myMap = [list(map(int,input().split())) for i in range(n)]
import copy
"""
n,m,d = 6,5,1
myMap = [[1,0,1,0,1],
         [0,1,0,1,0],
         [1,1,0,0,0],
         [0,0,0,1,1],
         [1,1,0,1,1],
         [0,0,1,0,0]]


"""
#조합??
# m개의 자라에 대해서 3자리에 대한 경우의 수만 뽑으면 됨
from itertools import combinations

#궁수 : 2, 적 : 1, 빈 자리 : 0
#1. 궁수 배치 함수
#2. 궁수 거리 함수
#3. 가장 가까운 적 제거 함수(왼쪽부터8방향)
#4. 적 이동 함수
# 모든 경우의 수에 대한 결과를 저장하고 max로 뽑기



dx = [0,-1,0,1]
dy = [-1,0,1,0]
from collections import deque


def update_d(gung_position,cnt):
    ggg = set()
    for ddd in gung_position:
        flag = False
        fff=set()
        for i in range(len(myMap)):
            for j in range(len(myMap[0])):
                if(0<=i and i<n and 0<=j and j<m):
                    #print("ddd[0]",ddd[0],"i",i,"ddd[1]",ddd[1],"j",j)
                    if((abs(i-ddd[0])+ abs(ddd[1]-j))<=d and myMap_second[i][j] == 1):
                        #print("i", i, "j", j, "visited[i][j]<=d", visited[i][j] <= d, "myMap_second[i][j]", myMap_second[i][j],
                        #      "myMap_second[i][j] == 1", myMap_second[i][j] == 1)
                        fff.add((i,j,abs(i-ddd[0]) + abs(ddd[1]-j)))
                        #print('i',i,'j',j)

        if(len(fff)):
            aaaa = [list(i) for i in fff]
            #print("before fff", aaaa)
            aaaa = sorted(aaaa,key=lambda x: (x[2],x[1]))
            #print("after fff", aaaa)
            ggg.add((aaaa[0][0],aaaa[0][1]))
    for i in ggg:
        myMap_second[i[0]][i[1]] = 0
        cnt += 1
    return cnt
def move():
    #print(myMap_second)
    myMap_second.pop(n - 1)
    #print(myMap_second)
    myMap_second.insert(0,[0 for j in range(m)])
    #print(myMap_second)


combi_c = [i for i in range(m)]
gungsu_position = combinations(combi_c,3)


result = set()
for comNum in gungsu_position:
    gung_position = [[n, comNum[0]], [n, comNum[1]], [n, comNum[2]]]
    myMap_second = copy.deepcopy(myMap)
    tmp = [2 if i == comNum[0] or i == comNum[1] or i == comNum[2] else 0 for i in range(m) ]
    myMap_second +=[tmp]
    cnt = 0
    #visited = [[0 for j in range(m)] for i in range(n)]
    #visited += [[0 for j in range(m)]]
    for jj in range(n):
    #for kk in range(3):

        # print("****************************************************************************************************")
        # print()
        # #print(gung_position[kk])
        # for i in range(len(visited)):
        #     for j in range(len(visited[0])):
        #         print(myMap_second[i][j], end=' ')
        #     print()
        # print("****************************************************************************************************")
        # print()
        q = deque(gung_position)
        #bfs_cal()
        cnt = update_d(gung_position,cnt)
        #cnt = update_d(gung_position,cnt)
        #cnt = update_d(gung_position,cnt)
            #myMap_second, cnt = update_d(myMap_second, cnt)
            #cnt =
            #cnt = update_d(cnt)


        # print("--------------------------cnt : ",cnt)
        # for i in range(len(visited)):
        #     for j in range(len(visited[0])):
        #         print(myMap_second[i][j], end=' ')
        #     print()
        # print("*************************")
        # print()
        # for i in range(len(visited)):
        #     for j in range(len(visited[0])):
        #         print(visited[i][j], end=' ')
        #     print()
        # print("#####################")
        # print()
        # print()
        move()
    result.add(cnt)

print(max(result))


#2시간  걸림
