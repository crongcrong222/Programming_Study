# -*- coding: utf-8 -*-
# 

import sys
input = sys.stdin.readline

INF = int(1e9)

#노드 갯수, 간선 갯수 입력 받기
n, m = map(int, input().split())

#시작 노드 번호 입력 받기
start = int(input())

#각 노드에 연결되어 있는 노드 정보를 담고 있는 리스트 만들기
graph = [[] for i in range(n + 1)]

#방문한 적이 있는지 체크하는 목적 리스트 만들기
visited = [False] * (n + 1)

#최단 거리 테이블을 모두 무한으로 초기화 하기
distance = [INF] * (n + 1)

#모든 간선 정보 입력 받기
for i in range(m):
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미임
    a, b, c = map(int, input().split())
    
    graph[a].append([b,c])

#방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환하는 함수
def get_smallest_node():
    minValue = INF
    
    #가장 최단 거리가 짧은 노드의 인덱스
    index = 0

    for i in range(1, n + 1):
        if(distance[i] < minValue) and (visited[i] == False):
            minValue = distance[i]
            index = i
    return index

def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for k in graph[start]:
        distance[k[0]] = k[1]

    #시작 노드를 제외하고 전체 n-1개의 노드에 대해 반복하기
    for i in range(n - 1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내, 방문 처리함
        now = get_smallest_node()
        visited[now] = True
        
        #현재 노드와 연결된 다른 노드를 확인함
        for j in graph[now]:
            cost = distance[now] + j[1]

            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧으면
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

#모든 노드로 가기 위해 최단 거리를 출력
for i in range(1, n + 1):
    #도달할 수 없는 경우에는 무한(INF)라고 출력함
    if(distance[i] == INF):
        print("INFINITY")
    else:
        print(distance[i])

