#dict = {치킨집 좌표 : 최소 치킨 거리의 합}
#0 : 빈 칸
#1 : 일반 집
#2 : 치킨 집

#전략!
#1. 치킨집 좌표 리스트, 일반집리스트 만들기
#2. 일반집을 기준으로 가장 가까운 치킨집(치킨집 좌표) 밸류에 최소 치킨 거리 더하기(bfs)
#3. value 기준으로 내림차순 정렬 한 후 폐업시키지 않을 치킨 집 갯 수 만큼 리스트 생성
#4. 가장 마지막에 있는 치킨집 거리 출력(최소 치킨 거리임)
'''
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
'''
from collections import deque
import itertools

#최대한.... itertools를 사용하지 말자


# MAF_0x02_No_Module_Combinations 사용
def combinations(arr,n):
    for i in range(len(arr)):#함수에서 할 일
        if n == 1:#종료조건
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], n-1):#다음에 할 일
                yield [arr[i]] + next



n, good_chi = map(int, input().split())

myMap = [list(map(int, input().split())) for _ in range(n)]


chiken = [[i,j] for i in range(n) for j in range(n) if myMap[i][j] == 2]
home_list = [[i,j] for i in range(n) for j in range(n) if myMap[i][j] == 1]

chi_list = list(combinations(chiken,good_chi))

#치킨집과 집 중에서 가장 짧은 거리 계산하기

def calc_distance(house, chicken_list):
    min_dis = 1e9
    for i in chicken_list:
        dist = abs(i[0]-house[0]) + abs(i[1] - house[1])
        min_dis = min(dist,min_dis)
    return min_dis


answer = []

for ch in chi_list:
    total = 0
    for h in home_list:
        total += calc_distance(h,ch)
    answer.append(total)

print(min(answer))