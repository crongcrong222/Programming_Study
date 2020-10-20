import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    tmp = 0
    while(scoville[0]<K):
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville,a + 2 * b)
        answer += 1
        if(scoville[0] <K and len(scoville) == 1):
            answer = -1
            return answer
    return answer



print(solution([1,2,3,9,10,12],7))

