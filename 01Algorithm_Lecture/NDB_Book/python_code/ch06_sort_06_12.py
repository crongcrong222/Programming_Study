import sys

n, cnt = map(int,sys.stdin.readline().split())

arr1 = list(map(int,sys.stdin.readline().split()))
arr2 = list(map(int,sys.stdin.readline().split()))

arr1 = sorted(arr1)
arr2 = sorted(arr2, reverse = True)

for i in range(cnt):
    if (arr1[i] < arr2[i]):
        arr1[i], arr2[i] = arr2[i], arr1[i]
    else:
        break

result = sum(arr1)
print(result)