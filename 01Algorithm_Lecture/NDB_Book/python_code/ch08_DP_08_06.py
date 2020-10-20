import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * 100

dp[0] = arr[0]
dp[1] = max(arr[0],arr[1])

for i in range(2, n):
    dp[i] = max(dp[i-1],dp[i-2] + arr[i])


print(dp[n-1])