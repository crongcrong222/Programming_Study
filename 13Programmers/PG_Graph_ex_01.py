#https://programmers.co.kr/learn/courses/30/lessons/49189


from collections import defaultdict,deque

def bfs(graph,start,visited,path):
    queue = deque([start])
    #처음 방문할 곳을 deque에 넣음
    
    
    while(queue):
        n = queue.popleft()
        visited[start] =True
        #방문을 하고(queue에서 꺼내고) 방문 체크를 함
        for i in graph[n]:
            #해당 방문한 그래프와 연결된 다른 그래프 숫자(노드)를 하나씩 꺼내서 확인
            if(visited[i] == False):
                #만약 해당 숫자(노드)를 방문하지 않았으면
                queue.append(i)
                visited[i] = True
                #방문 대기열(queue)에 추가하고 방문 여부를 체크
                path[i] = path[n] + 1
                #해당 그래프 숫자(노드)에 방문 횟수를 증가시킴

def solution(n, edge):
    graph = defaultdict(list)
    visited = [False for i in range(n+1)]
    #방문 여부를 체크하는 리스트 생성
    for i,j in edge:
        graph[i].append(j)
        graph[j].append(i)
    #방문 노드를 각각 추가함
    path = [0 for i in range(n+1)]
    bfs(graph,1,visited,path)
    print(path)
    return path.count(max(path))

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))