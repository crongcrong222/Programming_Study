import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    name, score = map(str,sys.stdin.readline().split())
    score = int(score)
    arr.append([name,score])

arr = sorted(arr, key = lambda x : x[1])

for i in range(n):
    print(arr[i][0], end = ' ')