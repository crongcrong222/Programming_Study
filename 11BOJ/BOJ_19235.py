import sys
n = int(sys.stdin.readline())
import copy
INF = 1e9
def transposeMatrix(arr1):
    arr = copy.deepcopy(arr1)
    r_len = len(arr)
    c_len = len(arr[0])
    tt = [[0] * r_len for i in range(c_len)]
    for i in range(r_len):
        for j in range(c_len):
            tt[j][i] = arr[i][j]
    return tt

def let_block(arr,block):
    tmp = transposeMatrix(arr)
    minLetr = len(arr)-1
    a = INF
    b = INF
    c = INF
    d = INF
    for b_r in block:
        for b_c in b_r:
            if (1 in tmp[b_c[2]]):
                a = tmp[b_c[2]].index(1) - 1
            if (2 in tmp[b_c[2]]):
                b = tmp[b_c[2]].index(2) - 1
            if (3 in tmp[b_c[2]]):
                c = tmp[b_c[2]].index(3) - 1
            if(sum(tmp[b_c[2]]) == 0):
                d = len(arr)-1
            minLetr = min (a,b,c,d,minLetr)
            tmp[b_c[2]][minLetr] = b_c[0]
        for b_c in b_r:
            arr[minLetr][b_c[2]] = b_c[0]
    return arr

def check_r_get_score(arr):
    global score
    flag = False
    for check_r in range(len(arr)-1, -1, -1):
        if not(0 in arr[check_r]):
            score += 1
            arr.pop(check_r)
            arr.insert(0,[0, 0, 0, 0])
            flag = True

    return arr,flag

def check_ddang(arr):
    tmp = transposeMatrix(arr)
    for i in range(4):
        if(2 in tmp[i]):
            continue
        for j in range(len(tmp[i])-1,1,-1):
            if(tmp[i][j] == 0):
                tmp[i].pop(j)
                tmp[i].insert(0,0)
    arr = transposeMatrix(tmp)
    return arr

def check_special_r(arr):
    special_r = [0,1]
    cnt_remove_r = 0
    for i in special_r:
        if(sum(arr[i]) != 0):
            cnt_remove_r += 1
    for shift_cnt in range(cnt_remove_r):
        arr.pop()
        arr.insert(0,[0,0,0,0])
    return arr

blocks = []
myMapRed = [[0] * 4 for i in range(6)]

tttttt = [[0] * 4 for i in range(6)]
score = 0
#진짜 블록 처럼 구성하기 위해 아래와 같이 블럭을 만듬
#len을 했을 때 진짜 블럭모양에 따른 길이가 나옴

for i in range(n):
    blocks = []
    blocksBlue = []
    ttt = list(map(int,sys.stdin.readline().split()))
    if(ttt[0] == 1):
        blocks.append([[ttt[0],ttt[1],ttt[2]]])
        blocksBlue.append([[ttt[0],ttt[1],3 - ttt[2]]])
    elif(ttt[0] == 2):
        blocks.append([[ttt[0],ttt[1],ttt[2]],[ttt[0],ttt[1],ttt[2]+1]])
        blocksBlue.append([[3, ttt[2], 3 - ttt[1]]])
        blocksBlue.append([[3, ttt[2] + 1, 3 - ttt[1]]])
    elif (ttt[0] == 3):
        blocks.append([[ttt[0], ttt[1], ttt[2]]])
        blocks.append([[ttt[0], ttt[1] + 1, ttt[2]]])
        blocksBlue.append([[2,ttt[2],3 - (ttt[1] + 1)],[2,ttt[2],3 - ttt[1]]])
    let_block(myMapRed, blocks)
    flag1 = True
    #while(flag1):
    myMapRed, flag1 = check_r_get_score(myMapRed)
    myMapRed = check_ddang(myMapRed)
    myMapRed = check_special_r(myMapRed)
    flag1 = True
    #while (flag1):
    myMapRed, flag1 = check_r_get_score(myMapRed)
    myMapRed = check_ddang(myMapRed)
    let_block(tttttt, blocksBlue)
    flag2 = True
    #while(flag2):
    tttttt,flag2 = check_r_get_score(tttttt)
    tttttt = check_ddang(tttttt)
    tttttt = check_special_r(tttttt)
    flag2 = True
    #while (flag2):
    tttttt, flag2 = check_r_get_score(tttttt)
    tttttt = check_ddang(tttttt)
#tttttt = transposeMatrix(tttttt)
result = 0
for i in range(len(myMapRed)):
    result += myMapRed[i].count(1)
    result += myMapRed[i].count(2)
    result += myMapRed[i].count(3)
    result += tttttt[i].count(1)
    result += tttttt[i].count(2)
    result += tttttt[i].count(3)


print(score)
print(result)


'''



#빨간 블록 먼저 만들고 파란 블록은 회전 시켜서 적용하자
#1. 블록 놓는 함수 ok
#2. 블록에 1행(열) 꽉 찼는지 검사하는 함수(점수 카운트 해야 함) ok
#3. 특별한 블록에 몇 행이나 있는지 검사하여 밀어버리는 함수(점수 카운트 x)
#4. 땡길 것이 있는지 검사하는 함수
#5. 지워지고 나서 같은 블록만 아래 경계까지 내려가게 하는 함수


import copy
INF = 1e9
def transposeMatrix(arr1):
    arr = copy.deepcopy(arr1)
    r_len = len(arr)
    c_len = len(arr[0])
    tt = [[0] * r_len for i in range(c_len)]
    for i in range(r_len):
        for j in range(c_len):
            tt[j][i] = arr[i][j]
    return tt

def check_ddang(arr):
    #행과 열 두가지를 검사하면서
    #열의 경우는 검사하기 쉽게 하기 위해 전치 행렬로 바꿈
    tmp = transposeMatrix(arr)


#len(blocks)는 행의 길이
#len(blocks[0])는 열의 길이
#print(len(blocks))
#print((blocks))
def let_block(arr,block):
    tmp = transposeMatrix(arr)
    minLetr = len(arr)-1
    a = INF
    b = INF
    c = INF
    d = INF
    for b_r in block:
        for b_c in b_r:
            #print("b_c[2]",b_c[2])
            #print("tmp[b_c[2]]",tmp[b_c[2]])
            if (1 in tmp[b_c[2]]):
                #print("--1--")
                a = tmp[b_c[2]].index(1) - 1
                #print("a",a)
            if (2 in tmp[b_c[2]]):
                #print("--2--")
                b = tmp[b_c[2]].index(2) - 1
                #print("b",b)
            if (3 in tmp[b_c[2]]):
                #print("--3--")
                c = tmp[b_c[2]].index(3) - 1
                #print("c",c)
            if(sum(tmp[b_c[2]]) == 0):
                #print("--4--")
                d = len(arr)-1
            minLetr = min (a,b,c,d,minLetr)
            #print("minLetr",minLetr)
            tmp[b_c[2]][minLetr] = b_c[0]
        for b_c in b_r:
            arr[minLetr][b_c[2]] = b_c[0]
            #print("arr[minLetr][b_c[2]] = b_c[0]",arr[minLetr][b_c[2]] ,b_c[0])
    return arr

def check_r_get_score(arr):
    global score
    flag = False
    for check_r in range(len(arr)-1, -1, -1):
        if not(0 in arr[check_r]):
            score += 1
            arr.pop(check_r)
            arr.insert(0,[0, 0, 0, 0])
            flag = True

    return arr,flag


def check_ddang_red(arr):
    tmp = transposeMatrix(arr)
    for i in range(4):
        cntt = 0
        if(2 in tmp[i]):
            continue
        for j in range(len(tmp[i])-1,1,-1):
            if(tmp[i][j] == 0):
                tmp[i].pop(j)
                tmp[i].insert(0,0)
    arr = transposeMatrix(tmp)
    return arr
def check_ddang_blue(arr):
    tmp = transposeMatrix(arr)
    for i in range(4):
        cntt = 0
        if(2 in tmp[i]):
            continue
        for j in range(len(tmp[i])-1,1,-1):
            if(tmp[i][j] == 0):
                tmp[i].pop(j)
                tmp[i].insert(0,0)
    arr = transposeMatrix(tmp)
    return arr

def check_special_r(arr):
    special_r = [0,1]
    cnt_remove_r = 0
    for i in special_r:
        if(sum(arr[i]) != 0):
            cnt_remove_r += 1
    for shift_cnt in range(cnt_remove_r):
        arr.pop()
        arr.insert(0,[0,0,0,0])
    return arr

'''

'''




blocks = []
myMapRed = [[0] * 4 for i in range(6)]

tttttt = copy.deepcopy(myMapRed)
score = 0
#진짜 블록 처럼 구성하기 위해 아래와 같이 블럭을 만듬
#len을 했을 때 진짜 블럭모양에 따른 길이가 나옴

for i in range(n):
    blocks = []
    blocksBlue = []
    ttt = list(map(int,input().split()))
    if(ttt[0] == 1):
        blocks.append([[ttt[0],ttt[1],ttt[2]]])
        blocksBlue.append([[ttt[0],ttt[1],3 - ttt[2]]])
    elif(ttt[0] == 2):
        blocks.append([[ttt[0],ttt[1],ttt[2]],[ttt[0],ttt[1],ttt[2]+1]])
        blocksBlue.append([[3, ttt[2], 3 - ttt[1]]])
        blocksBlue.append([[3, ttt[2] + 1, 3 - ttt[1]]])
    elif (ttt[0] == 3):
        blocks.append([[ttt[0], ttt[1], ttt[2]]])
        blocks.append([[ttt[0], ttt[1] + 1, ttt[2]]])
        blocksBlue.append([[2,ttt[2],3 - (ttt[1] + 1)],[2,ttt[2],3 - ttt[1]]])
    flag1 = True
    flag2 = True
    #print("blocks is -> ",blocks)
    #print("blocksBlue is -> ", blocksBlue)
    let_block(myMapRed, blocks)
    #print("let_block ok-----------------------")
    #print('-------------')
    #for i in range(len(myMapRed)):
    #    for j in range(len(myMapRed[0])):
    #        print(myMapRed[i][j], end=' ')
    #    print()
    flag1 = True
    while(flag1):
        myMapRed, flag1 = check_r_get_score(myMapRed)
        myMapRed = check_ddang_red(myMapRed)

    #print("check_r_get_score ok`````````````````")
    #print('-------------')
    #for i in range(len(myMapRed)):
    #    for j in range(len(myMapRed[0])):
    #        print(myMapRed[i][j], end=' ')
    #    print()

    myMapRed = check_special_r(myMapRed)
    #print("check_special_r cehckaaaaaaaaaaaaaaaaaaaaa")
    #print('-------------')
    #for i in range(len(myMapRed)):
    #    for j in range(len(myMapRed[0])):
    #        print(myMapRed[i][j], end=' ')
    #    print()
    flag1 = True
    while (flag1):
        myMapRed, flag1 = check_r_get_score(myMapRed)
        myMapRed = check_ddang_red(myMapRed)
    #print("blocks",blocks)
    #print("blocksBlue",blocksBlue)
    #print()
    #print("#############################################")
    #print("blocksBlue is -> ", blocksBlue)
    let_block(tttttt, blocksBlue)

    #print("let_block ok-----------------------")
    #print('-------------')
    #for i in range(len(tttttt)):
    #    for j in range(len(tttttt[0])):
    #        print(tttttt[i][j], end=' ')
    #    print()
    flag2 = True
    while(flag2):
        tttttt,flag2 = check_r_get_score(tttttt)
        tttttt = check_ddang_blue(tttttt)
    #print("check_r_get_score ok-----------------------")
    #print('-------------')
    #for i in range(len(tttttt)):
    #    for j in range(len(tttttt[0])):
    #        print(tttttt[i][j], end=' ')
    #    print()
    tttttt = check_special_r(tttttt)

    #print("check_special_r ok-----------------------")
    #print('-------------')
    #for i in range(len(tttttt)):
    #    for j in range(len(tttttt[0])):
    #        print(tttttt[i][j], end=' ')
    #    print()
    #print()
    flag2 = True
    while (flag2):
        tttttt, flag2 = check_r_get_score(tttttt)
        tttttt = check_ddang_blue(tttttt)

#print("#############################################")
#print("#############################################")
#print("#############################################")

#for i in range(len(myMapRed)):
#    for j in range(len(myMapRed[0])):
#        print(myMapRed[i][j], end=' ')
#    print()
#print(';;;;;;;;;;;;;;;;;;;;;;;')
tttttt = transposeMatrix(tttttt)
#for i in range(len(tttttt)):
#    for j in range(len(tttttt[0])):
#        print(tttttt[i][j], end=' ')
#    print()

result = 0
for i in range(len(myMapRed)):
    result += myMapRed[i].count(1)
    result += myMapRed[i].count(2)
    result += myMapRed[i].count(3)
for i in range(len(tttttt)):
    result += tttttt[i].count(1)
    result += tttttt[i].count(2)
    result += tttttt[i].count(3)
print(score)
print(result)



n = int(input())

#빨간 블록 먼저 만들고 파란 블록은 회전 시켜서 적용하자
#1. 블록 놓는 함수 ok
#2. 블록에 1행(열) 꽉 찼는지 검사하는 함수(점수 카운트 해야 함) ok
#3. 특별한 블록에 몇 행이나 있는지 검사하여 밀어버리는 함수(점수 카운트 x)
#4. 땡길 것이 있는지 검사하는 함수
#5. 지워지고 나서 같은 블록만 아래 경계까지 내려가게 하는 함수





'''