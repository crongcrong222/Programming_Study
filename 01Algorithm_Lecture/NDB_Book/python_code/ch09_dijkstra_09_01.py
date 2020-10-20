# -*- coding: utf-8 -*-
# 

import sys
input = sys.stdin.readline

INF = int(1e9)

#��� ����, ���� ���� �Է� �ޱ�
n, m = map(int, input().split())

#���� ��� ��ȣ �Է� �ޱ�
start = int(input())

#�� ��忡 ����Ǿ� �ִ� ��� ������ ��� �ִ� ����Ʈ �����
graph = [[] for i in range(n + 1)]

#�湮�� ���� �ִ��� üũ�ϴ� ���� ����Ʈ �����
visited = [False] * (n + 1)

#�ִ� �Ÿ� ���̺��� ��� �������� �ʱ�ȭ �ϱ�
distance = [INF] * (n + 1)

#��� ���� ���� �Է� �ޱ�
for i in range(m):
    #a�� ��忡�� b�� ���� ���� ����� c��� �ǹ���
    a, b, c = map(int, input().split())
    
    graph[a].append([b,c])

#�湮���� ���� ��� �߿���, ���� �ִ� �Ÿ��� ª�� ����� ��ȣ�� ��ȯ�ϴ� �Լ�
def get_smallest_node():
    minValue = INF
    
    #���� �ִ� �Ÿ��� ª�� ����� �ε���
    index = 0

    for i in range(1, n + 1):
        if(distance[i] < minValue) and (visited[i] == False):
            minValue = distance[i]
            index = i
    return index

def dijkstra(start):
    #���� ��忡 ���ؼ� �ʱ�ȭ
    distance[start] = 0
    visited[start] = True
    for k in graph[start]:
        distance[k[0]] = k[1]

    #���� ��带 �����ϰ� ��ü n-1���� ��忡 ���� �ݺ��ϱ�
    for i in range(n - 1):
        #���� �ִ� �Ÿ��� ���� ª�� ��带 ����, �湮 ó����
        now = get_smallest_node()
        visited[now] = True
        
        #���� ���� ����� �ٸ� ��带 Ȯ����
        for j in graph[now]:
            cost = distance[now] + j[1]

            #���� ��带 ���ļ� �ٸ� ���� �̵��ϴ� �Ÿ��� �� ª����
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

#��� ���� ���� ���� �ִ� �Ÿ��� ���
for i in range(1, n + 1):
    #������ �� ���� ��쿡�� ����(INF)��� �����
    if(distance[i] == INF):
        print("INFINITY")
    else:
        print(distance[i])

