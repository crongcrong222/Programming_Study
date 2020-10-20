import sys
import copy
def solution(n,m):
    mm = 1e9+7
    
    DP = [[0 for col in range(1001)] for row in range(1001)]

    DP[1][1] = 1
    
    for i in range(5):
        for j in range(5):
            print(DP[i][j], end = ' ')
        print()
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if(i != 1 or j != 1):
                DP[i][j] = (DP[i][j-1]%mm + DP[i-1][j]%mm + DP[i-1][j-1]%mm)%mm

    return DP[n][m]%mm
                





n,m = map(int, sys.stdin.readline().split())



print(solution(n,m))
