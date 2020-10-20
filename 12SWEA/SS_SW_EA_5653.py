# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.



for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    time = 0
    myMap = [[None] * (m + k) for i in range(n+k)]
    #0 : 빈 공간, 1:비활성, 2: 활성, 3:죽은 상태
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(len(tmp)):
            myMap[i + k//2][j + k//2] = tmp[j]
            #q.put([tmp[j],1,0,[i + k//2,j + k//2]])
            #[hp,상태,지난시간, position]


    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    #active에 활성화된 세포들을 넣기
    active = [[] for i in range(11)]
    for i in range(n + k):
        for j in range(m + k):
                if myMap[i][j]:
                    #만약 활성화된 세포가 있으면
                    active[myMap[i][j]].append([i, j, myMap[i][j]])
                    #active에 position 정보와 세포의 hp 정보를 append
    #k만큼 지남
    for i in range(k):
        for power in range(10,0,-1):
            #생명력이 가장 큰 것 부터 번식 시작
            cells = active[power]
            new=[]
            #활성화가 시작된, 번식된 세포들을 저장함
            old=[]
            #죽은 세포를 저장함
            for j in range(len(cells)-1,-1,-1):
                cells[j][2] -=1
                #hp를 감소시킴
                x,y,hp = cells[j]
                if hp == -1:
                    #hp가 + 상태면 비활성화이고, -상태이면 활성화 시작
                    #활성화를 하면서 번식 시작
                    for dir in range(4):
                        cx = x + dx[dir]
                        cy = y + dy[dir]
                        if(not myMap[cx][cy]):
                            #만약 다음 공간이 빈 공간이면
                            myMap[cx][cy] = power
                            new.append([cx,cy,power])
                            #번식을 하고, 번식된 세포의 정보를 new에 저장
                if hp == -power:
                    #만약 활성화 최대 hp에 도달하면
                    old.append(j)
                    #죽은 세포로 간주해서 old에 저장

            for idx in old:
                #해당 우선순위(높은 hp)의 번식, 활성화가 끝났으면
                #old에 있는 cells를 버리기
                cells.pop(idx)
            active[power] += new
            #call of reference(함수 호출 방식)
            #active[power] += new로 해도 괜찮음
            #번식된 최신 세포의 정보를 cells에 저장

    result = 0
    for i in range(1, 11):
        result += len(active[i])
    print("#{} {}".format(test_case,result))