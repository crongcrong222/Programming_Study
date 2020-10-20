import sys
n = int(sys.stdin.readline().rstrip())
#n = int(input())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline().rstrip()))
    #a.append(int(input()))

'''
def QuickSort(sortList):
    if len(sortList) < 2:
        return sortList

    pivot= sortList[0]

    less = [i for i in sortList[1:] if i <=pivot]
    greater = [i for i in sortList[1:] if i > pivot]

    sortList = QuickSort(less) + [pivot] + QuickSort(greater)
    return sortList'''

'''
def BubbleSort(n, sortList):
    for i in range(n-1):
        for j in range(n-1-i):
            if( sortList[j] > sortList[j+1]):
                sortList[j], sortList[j+1] = sortList[j+1], sortList[j]
    return sortList'''


def mergeSort(sortList):
    if len(sortList)< 2:
        return sortList

    mid = len(sortList)//2
    left = mergeSort(sortList[:mid])
    right = mergeSort(sortList[mid:])

    i,j,k = 0,0,0

    while i <len(left) and j < len(right):
        if(left[i]<right[j]):
           sortList[k] = left[i]
           i+=1
        else:
            sortList[k] = right[j]
            j+=1
        k+=1
    if i == len(left):
        while j < len(right):
            sortList[k] = right[j]
            j+=1
            k+=1
    elif j == len(right):
        while i < len(left):
            sortList[k] = left[i]
            i+=1
            k+=1 
    return sortList

b = mergeSort(a)

for i in b:
    print(i)
