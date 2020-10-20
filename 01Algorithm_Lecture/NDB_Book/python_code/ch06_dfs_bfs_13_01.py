# -*- coding: utf-8 -*-4
from collections import deque

# ������ ����, ������ ����, �Ÿ� ����, ��� ���� ��ȣ
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# ��� ���� ���� �Է� �ޱ�
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# ��� ���ÿ� ���� �ִ� �Ÿ� �ʱ�ȭ
distance = [-1] * (n + 1)
distance[x] = 0 # ��� ���ñ����� �Ÿ��� 0���� ����

# �ʺ� �켱 Ž��(BFS) ����
q = deque([x])
while q:
    now = q.popleft()
    # ���� ���ÿ��� �̵��� �� �ִ� ��� ���ø� Ȯ��
    print(graph)
    for next_node in graph[now]:
        # ���� �湮���� ���� ���ö��
        
        if distance[next_node] == -1:
            # �ִ� �Ÿ� ����
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# �ִ� �Ÿ��� K�� ��� ������ ��ȣ�� ������������ ���
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# ���� �ִ� �Ÿ��� K�� ���ð� ���ٸ�, -1 ���
if check == False:
    print(-1)