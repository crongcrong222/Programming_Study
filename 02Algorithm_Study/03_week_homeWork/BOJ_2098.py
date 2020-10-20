import sys

sys.setrecursionlimit(10000)
INF=sys.maxsize

n = int(sys.stdin.readline().rstrip())

myMap = [list(map(int,sys.stdin.readline().split()))for i in range(n)]


dp = [[INF]*(1<<n)for i in range(n)]
#가장 큰 수들로 리스트 만들기

def dfs(cur, visit):
    if (visit == (1<<n)-1):
        # 1번째부터 n번째까지 모두 순회된 것 확인
        if(myMap[cur][0] == 0):
            # 다 돌고 cur번째에서 돌아올 수 있는지 확인
            # 0이면 돌아올 수 있는 길이 없기 때문에 INF 반환
            return INF
        else:
            return myMap[cur][0]
    if (dp[cur][visit] != INF):
        return dp[cur][visit]
        #결과 값을 dp 리스트에 저장
    
    for i in range(1,n):
        if(not visit&(1<<i)) and (myMap[cur][i]!=0):
            # 방문하지 않고 가는 길이 있으면,
            dp[cur][visit] = min(dp[cur][visit],
                                 dfs(i,visit|(1<<i)) + myMap[cur][i])
            # 방문하는 곳의 비용은  두 값 중 최소 값
    return dp[cur][visit]
print(dfs(0,1))
    
