import sys,heapq

min_heap = []
max_heap = []


input = sys.stdin.readline

n = int(input())

heap= []
for i in range(n):
    tmp = int(input())
    if(len(max_heap) == len(min_heap)):
        heapq.heappush(max_heap,(-i,i))
    else:
        heapq.heappush(min_heap,(i,i))

    if (len(min_heap) >1) and min_heap[0][1]<max_heap[0][1]:
        maxx = heapq.heappop(max_heap)[1]
        minn = heapq.heappop(min_heap)[1]
        heapq.heappush(min_heap, (maxx, maxx))
        heapq.heappush(max_heap, (-minn, minn))
    print(max_heap[0][1])
