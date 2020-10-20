'''
i일째 받을 수 있는 최대 금액 DP[i] 
1. 일을 안하고넘어감 DP[i] == D[i+1] 
2. 일을 하고 넘어감 DP[i] == P[i] + DP[i + T[i]]
1과 2중 큰 값을 DP[i] 정의함
'''


from sys import stdin
def solution(day,T,P):
    T.append(0)
    P.append(0)
    
    # 마지막 날 다음 날은 정산 받는 날
    # 정산 받는 날에 대해 T, P의 값을 넣음

    DP = [0] * (day + 2)
    #계산된 값이 저장될 리스트 DP
    
    for i in  range(day,0,-1):
        if(i + T[i] > day + 1):
            DP[i] = DP[i + 1]
        else:
            DP[i] = max(DP[i+1], (P[i]+DP[i+T[i]]))
    return DP[1]






day = int(stdin.readline().rstrip())
T = [0]
P = [0]

# 0일 째가 아닌 1일 째부터 날짜 계산을 쉽게 하기 위해 0번째 리스트 값에
# 0을 삽입
for i in range(day):
    a,b = list(map(int, stdin.readline().split()))
    T.append(a)
    P.append(b)

print(solution(day,T,P))
