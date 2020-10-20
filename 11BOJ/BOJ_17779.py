n = int(input())

#https://www.acmicpc.net/status?user_id=aries904&problem_id=17779&from_mine=1

def solve(x,y,d1,d2):
    cntMap = [0 for i in range(5)]
    tmpMap = [[0 for i in range(n)] for j in range(n)]

    for i in range(d1 + 1):
        tmpMap[x+i][y-i] = 5
        tmpMap[x+i+d2][y+d2-i] = 5
    for i in range(d2 + 1):
        tmpMap[x+i][y+i] = 5
        tmpMap[x+i+d1][y+i-d1]=5
    for i in range(d1):
        tt = 1
        # 사선으로 채우기
        while (tmpMap[x + i + tt][y - i] != 5):
            tmpMap[x + i + tt][y - i] = 5
            tt += 1
    for i in range(d2):
        tt = 1
        #사선으로 채우기
        while(tmpMap[x+i + tt][y+i] != 5):
            tmpMap[x + i + tt][y + i] = 5
            tt += 1
    for i in range(n):
        for j in range(n):
            if (i < x + d1 and j <= y and tmpMap[i][j] == 0):
                tmpMap[i][j] = 1
            elif (i <= x + d2 and j > y and tmpMap[i][j] == 0):
                tmpMap[i][j] = 2
            elif (x + d1<=i and j < y -d1 +d2 and tmpMap[i][j] == 0):
                tmpMap[i][j] = 3
            elif (x + d2<i and y-d1+d2<=j and tmpMap[i][j] == 0):
                tmpMap[i][j] = 4
    for i in range(n):
        for j in range(n):
            cntMap[tmpMap[i][j]-1] += myMap[i][j]
    #print("cntMap",cntMap)
    # for i in range(n):
    #     for j in range(n):
    #         print(tmpMap[i][j] , end=' ')
    #     print()
    #print("A---------------------------------")
    return max(cntMap)-min(cntMap)


myMap= [list(map(int,input().split())) for j in range(n)]
answer = -1
result = set()
for x in range(n-2):
    for y in range(1,n-1):
        for d1 in range(1,y+1):
            for d2 in range(1,n-x-d1):
                if (d1>=1 and d2>=1 and x>=0and x+d1+d2<n and d1<=y and y-d1<y and y+d2<n):
                #try:
                    tttt = solve(x,y,d1,d2)
                    result.add(tttt)
                    if answer == -1:
                        answer =tttt
                    elif answer>tttt:
                        answer = tttt
                #except:
                #    continue
print(min(result))
#print(tttt)