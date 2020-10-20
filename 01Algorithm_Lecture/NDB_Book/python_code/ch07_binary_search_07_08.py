import sys

def binary_search(arr, target, start, end):
    if(start>end):
        return None
    mid = (start  + end)//2
    rice_son = sum(list(map(lambda x : x - mid if x > mid else 0, arr)))
    #print(rice_son)
    if(rice_son == target):
        return mid
    elif(rice_son < target):
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


n, son = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

print(binary_search(arr,son,0,max(arr)))
