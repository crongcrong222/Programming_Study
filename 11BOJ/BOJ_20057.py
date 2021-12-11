# def rotate(arr):
#     tmpArr = [[0] * len(arr) for i in range(len(arr))]
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             tmpArr[j][-1-i] = arr[i][j]
#     return tmpArr
#
# def rotate_reverse(arr):
#     m = len(arr)
#     tmparr = [[0] * m for i in range(m)]
#
#     for i in range(m):
#         for j in range(m):
#             tmparr[-1-j][i] = arr[i][j]
#     return tmparr
#
n = int(input())
# myMap = [[0] * n for i in range(n)]
myMap = [list(map(int,input().split())) for i in range(n)]
#
sy, sx = n//2, n//2
#
dir = [[0,-1],[1,0],[0,1],[-1,0]]
wind = [[[-1,0,0.07],[1,0,0.07],[-1,1,0.01],[1,1,0.01],[-1,-1,0.1],[1,-1,0.1],[0,-2,0.05],[-2,0,0.02],[2,0,0.02]],
        [[0,-1,0.07],[0,1,0.07],[-1,-1,0.01],[-1,1,0.01],[1,1,0.1],[1,-1,0.1],[2,0,0.05],[0,-2,0.02],[0,2,0.02]],
        [[-1,0,0.07],[1,0,0.07],[-1,-1,0.01],[1,-1,0.01],[-1,1,0.1],[1,1,0.1],[0,2,0.05],[-2,0,0.02],[2,0,0.02]],
        [[0,-1,0.07],[0,1,0.07],[1,-1,0.01],[1,1,0.01],[-1,-1,0.1],[-1,1,0.1],[-2,0,0.05],[0,-2,0.02],[0,2,0.02]]]

kkk = []
for i in range(1,n):
    kkk.append(i)
    kkk.append(i)
kkk.append(n-1)


result = 0
dic = 0
count = 1




total = 0
for i in range(len(myMap)):
    total += sum(myMap[i])


for num in kkk:
    for k in range(num):
        # print("k",k)
        ny, nx = sy + dir[dic%4][0], sx + dir[dic%4][1]
        # print("sx : ",sx, "sy : ", sy)
        # print("dic : ", dic, "nx : ", nx, "ny : ", ny)
        morea = 0
        for i in range(len(wind[0])):
            sel_wind = wind[dic % 4]
            my, mx = ny + sel_wind[i][0], nx + sel_wind[i][1]
            if mx >= 0 and mx < n and my >= 0 and my < n:
                myMap[my][mx] += int(float(myMap[ny][nx]) * sel_wind[i][2])
                morea += int(float(myMap[ny][nx]) * sel_wind[i][2])
            else:
                morea += int(float(myMap[ny][nx]) * sel_wind[i][2])
                result += int(float(myMap[ny][nx]) * sel_wind[i][2])
        myMap[ny][nx] -= morea
        my, mx = ny + dir[dic % 4][0], nx + dir[dic % 4][1]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if mx >= 0 and mx < n and my >= 0 and my < n:
                # print("---------- my : ",my, " mx : ", mx)
                myMap[my][mx] += myMap[ny][nx]
                myMap[ny][nx] = 0
            else:
                result += myMap[ny][nx]
                myMap[ny][nx] = 0
        # for y in range(n):
        #     for x in range(n):
        #         print(myMap[y][x], end='\t')
        #     print()
        # print("-----")
        sy, sx = ny, nx

        count += 1
    # tmp = 0
    # for i in range(len(myMap)):
    #     tmp += sum(myMap[i])
    # print("result", result, " total : ",total,"tmp total : ",tmp )
    dic += 1
print(result)



