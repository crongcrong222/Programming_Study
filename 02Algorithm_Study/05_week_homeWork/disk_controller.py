import heapq
def solution(jobs):
    answer = 0
    time = 0
    end = -1
    cnt = 0
    heap = []
    length = len(jobs)

    while(cnt < length):
        for i in jobs:
            inputTime = i[0]
            executingTime = i[1]
            if(end < inputTime <=time):
                answer += time - inputTime
                heapq.heappush(heap,executingTime)
        if(heap):
            answer += len(heap)*heap[0]
            end = time
            time += heapq.heappop(heap)
            cnt += 1
        else:
            time += 1
    return int(answer/length)



print(solution([[0, 3], [1, 9], [2, 6]]))
