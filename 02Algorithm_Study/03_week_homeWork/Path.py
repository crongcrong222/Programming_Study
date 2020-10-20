def solution(m, n, puddles):
    myMap = [[0 for i in range(m + 1)] for j in range(n + 1)]
    visit = myMap[:]
    visit[1][1] = 1

    for mul in puddles:
        myMap[mul[1]][mul[0]] = 1

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if(x !=1 or y != 1):
                if(myMap[x][y] == 1):
                    visit[x][y] = 0
                else:
                    visit[x][y] = (visit[x-1][y] + visit[x][y-1])%1000000007
    
    answer = visit[n][m]
    return answer


print(solution(4,3,[[2, 2]]))
