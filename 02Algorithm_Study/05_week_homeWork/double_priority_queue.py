import heapq
def solution(operations):
    answer = []
    heap = []
    for i in operations:
        op, n = map(str,i.split())
        n = int(n)
        if(op  == "I"):
           heapq.heappush(heap,n)
        else:
            if(len(heap)>0):
                if(n == 1):
                    heap.pop(heap.index(heapq.nlargest(1,heap)[0]))
                elif(n == -1):
                    heap.pop(heap.index(heapq.nsmallest(1,heap)[0]))
    if(len(heap)==0):
        return [0,0]
    else:
        return [heapq.nlargest(1,heap)[0],heapq.nsmallest(1,heap)[0]]
print(
solution(["I 7","I 5","I -5","D -1"])
)
