#https://programmers.co.kr/learn/courses/30/lessons/49189


from collections import defaultdict,deque

def bfs(graph,start,visited,path):
    queue = deque([start])
    #ó�� �湮�� ���� deque�� ����
    
    
    while(queue):
        n = queue.popleft()
        visited[start] =True
        #�湮�� �ϰ�(queue���� ������) �湮 üũ�� ��
        for i in graph[n]:
            #�ش� �湮�� �׷����� ����� �ٸ� �׷��� ����(���)�� �ϳ��� ������ Ȯ��
            if(visited[i] == False):
                #���� �ش� ����(���)�� �湮���� �ʾ�����
                queue.append(i)
                visited[i] = True
                #�湮 ��⿭(queue)�� �߰��ϰ� �湮 ���θ� üũ
                path[i] = path[n] + 1
                #�ش� �׷��� ����(���)�� �湮 Ƚ���� ������Ŵ

def solution(n, edge):
    graph = defaultdict(list)
    visited = [False for i in range(n+1)]
    #�湮 ���θ� üũ�ϴ� ����Ʈ ����
    for i,j in edge:
        graph[i].append(j)
        graph[j].append(i)
    #�湮 ��带 ���� �߰���
    path = [0 for i in range(n+1)]
    bfs(graph,1,visited,path)
    print(path)
    return path.count(max(path))

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))