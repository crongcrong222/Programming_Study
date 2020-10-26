def solution(n, computers):
    answer = 0

    q = []
    visited = [0 for i in range(n)]

    while( 0 in visited):
        #모든 지점을 방문할 때까지 반복
        idx = visited.index(0)
        #방문하지 않은 지점의 index 찾기
        q.append(idx)
        #큐에 추가
        visited[idx] = 1
        #방문 표시
        while(q):
            #큐에 들어가서 연결된 모든 지점을 방문할 때까지 반복
            com = q.pop(0)
            for i in range(n):
                if(visited[i] == 0 and computers[idx][i] == 1):
                    q.append(i)
                    visited[i] = 1
        answer+=1
    return answer


print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
