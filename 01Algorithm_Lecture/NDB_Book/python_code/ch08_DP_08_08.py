import sys

n, target = map(int, sys.stdin.readline().split())
money = [10001] * (target + 1)
money[0] = 0

tmp = [int(sys.stdin.readline().rstrip()) for i in range(n)]

for i in range(n):
    for j in range(tmp[i], target + 1):
        if(money[j - tmp[i]] != 10001):
            money[j] = min(money[j], money[j - tmp[i]] + 1)

print(money)
if( money[target] == 10001):
    print(-1)
else:
    print(money[target])