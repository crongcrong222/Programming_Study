from collections import defaultdict,deque

def solution(n, results):
    answer = 0
    win = defaultdict(set)
    lose = defaultdict(set)
    for i,j in results:
        win[i].add(j)
        lose[j].add(i)
    for i in range(1,n+1):
        for lo in win[i]:
            #�̱� ����� ������ 1�� �� ����
            lose[lo] |= lose[i]
            #��ü�� ��ĵ�ϸ鼭 �̱� ����� ������ �� ��� ����Ʈ�� ���� ���� �� ����Ʈ�� �߰�
        for wi in lose[i]:
            #�� ����� ������ 1�� �� ����
            win[wi] |= win[i]
            #��ü�� ��ĵ�ϸ鼭 �� ����� ������ �̱� ��� ����Ʈ�� ���� ���� �̱� ����Ʈ�� �߰�


    #print(win)
    #print(lose)
    result = [len(win[i]|lose[i]) for i in range(1,n+1)]
    answer = result.count(n-1)
    #�ڱ� �ڽ��� �����Ͽ� ����� ������� ���� ��� ī��Ʈ
    return answer


print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))