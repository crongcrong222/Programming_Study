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
            #이긴 사람의 상대방을 1개 씩 꺼냄
            lose[lo] |= lose[i]
            #전체를 스캔하면서 이긴 사람의 상대방이 진 사람 리스트를 꺼낸 상대방 진 리스트에 추가
        for wi in lose[i]:
            #진 사람의 상대방을 1개 씩 꺼냄
            win[wi] |= win[i]
            #전체를 스캔하면서 진 사람의 상대방이 이긴 사람 리스트를 꺼낸 상대방 이긴 리스트에 추가


    #print(win)
    #print(lose)
    result = [len(win[i]|lose[i]) for i in range(1,n+1)]
    answer = result.count(n-1)
    #자기 자신을 제외하여 대결한 사람들의 수를 세어서 카운트
    return answer


print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))