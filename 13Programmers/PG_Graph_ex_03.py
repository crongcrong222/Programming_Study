dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def direction(dir):
    return (dir + 1) % 8


from collections import defaultdict


def solution(arrows):
    answer = 0
    check = defaultdict(int)
    visit = defaultdict(int)
    preArrow = (0, 0)
    visit[preArrow] = 1

    for arr in arrows:
        for i in range(2):
            # 2배로 늘리기
            nowArrow = (preArrow[0] + dx[arr], preArrow[1] + dy[arr])
            if (visit[nowArrow] and not (preArrow, nowArrow) in check):
                answer += 1
            visit[nowArrow] = 1
            check[(preArrow, nowArrow)] = 1
            check[(nowArrow, preArrow)] = 1
            preArrow = nowArrow

    return answer





print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))