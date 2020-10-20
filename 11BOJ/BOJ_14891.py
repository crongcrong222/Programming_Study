myMap = [list(map(int, list(input()))) for i in range(4)]

#1. 회전 함수
#2. 옆에 있는 톱니 n-s, s-n 인지 또는 같은 것 확인 함수
roList=[0,0,0,0]
def topniRot(topni, dir):
    for i in range(4):
        if (dir[i] == 1):
            tmp = topni[i][-1]
            topni[i].pop()
            topni[i].insert(0, tmp)
        elif (dir[i] == -1):
            tmp = [topni[i][0]]
            topni[i].pop(0)
            topni[i] += tmp
    return topni

def check_other_rot(topn,state, toprotLst):

    if (topn == 0):
        toprotLst[0] = state
        state = -state
        if(myMap[0][2] != myMap[1][6]):
            toprotLst[1] = state
            state = -state
            if(myMap[1][2] != myMap[2][6]):
                toprotLst[2] = state
                state = -state
                if (myMap[2][2] != myMap[3][6]):
                    toprotLst[3] = state

    elif (topn == 1):
        toprotLst[1] = state
        state2 = -state
        if (myMap[0][2] != myMap[1][6]):
            toprotLst[0] = state2
        if(myMap[1][2] != myMap[2][6]):
            toprotLst[2] = state2
            state2 = -state2
            if(myMap[2][2] != myMap[3][6]):
                toprotLst[3] = state2

    elif (topn == 2):
        toprotLst[2] = state
        state2 = -state
        if(myMap[1][2] != myMap[2][6]):
            toprotLst[1] = state2
            state2 = -state2
            if (myMap[0][2] != myMap[1][6]):
                toprotLst[0] = state2
        if(myMap[2][2] != myMap[3][6]):
            toprotLst[3] = -state
    elif (topn == 3):
        toprotLst[3] = state
        state2 = -state
        if (myMap[2][2] != myMap[3][6]):
            toprotLst[2] = state2
            state2 = -state2
            if(myMap[1][2] != myMap[2][6]):
                toprotLst[1] = state2
                state2 = -state2
                if (myMap[0][2] != myMap[1][6]):
                    toprotLst[0] = state2

    return toprotLst
n = int(input())
for i in range(n):
    topNum, ddd = map(int, input().split())
    topNum -= 1
    #2, 6번째만 확인하면 됨
    #2의 옆 (2 + 6) % 12
    #6의 옆 (6 + 6) % 12
    #시계방향은 -> 반시계방향은 <-

    roList = check_other_rot(topNum,ddd,roList)
    myMap = topniRot(myMap,roList)
    roList = [0, 0, 0, 0]


print(myMap[0][0] * 1 + myMap[1][0] * 2 + myMap[2][0] * 4 + myMap[3][0] * 8)