class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap,(-i,i))

        while(len(heap)>1):
            first = heapq.heappop(heap)[1]
            second = heapq.heappop(heap)[1]
            if(first != second):
                tmp = first - second
                heapq.heappush(heap,(-tmp,tmp))

        if(len(heap) == 0):
            return 0
        else:
            return heap[0][1]
