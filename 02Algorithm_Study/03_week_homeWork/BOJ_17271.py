import sys

def solution(second, masic):
	dp = [0 for i in range(1000111)]
	dp[0] = 1
	for i in range(1, second+1):
		dp[i] = dp[i-1]
		if (i-masic >=0):
			dp[i] = (dp[i] + dp[i-masic])%1000000007
	return dp[second]
	
	
n,m = map(int, sys.stdin.readline().split())
print(solution(n,m))
