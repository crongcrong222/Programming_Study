import sys, heapq

heap = []

n = int(sys.stdin.readline())

for i in range(n):
    tmp = int(sys.stdin.readline())
    if( tmp != 0):
        heapq.heappush(heap,(abs(tmp),tmp))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
        
            

