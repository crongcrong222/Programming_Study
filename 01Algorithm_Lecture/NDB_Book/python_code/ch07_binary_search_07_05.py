'''
import sys

def binary_search(arr, target, start, end):
    if(start>end):
        return None
    mid = (start + end)//2
    if(arr[mid] == target):
        return target
    elif(arr[mid]>target):
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)



n = int(sys.stdin.readline().rstrip())
dong = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline().rstrip())

son = list(map(int,sys.stdin.readline().split()))


for i in son:
    result = binary_search(dong,i,0,n-1)
    if(result == None):
        print("No", end = ' ')
    else:
        print("Yes", end = ' ')



'''
'''
import sys
n = int(sys.stdin.readline().rstrip())
dong = [0] * 1000000

for i in sys.stdin.readline().split():
    dong[int(i)] = 1

m = int(sys.stdin.readline().rstrip())

son = list(map(int,sys.stdin.readline().split()))

for i in son:
    if(dong[i] == 1):
        print("Yes", end= ' ')
    else:
        print("No", end = ' ')
'''



import sys
n = int(sys.stdin.readline().rstrip())
dong = set(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline().rstrip())

son = list(map(int,sys.stdin.readline().split()))

for i in son:
    if(i in dong):
        print("Yes", end = ' ')
    else:
        print("No", end = ' ')