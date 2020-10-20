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
#sys.stdin = open("input.txt", "r")
from collections import defaultdict
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.


dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def update(myMap,recog,now_x,now_y):
    can_be_change = []
    for i in range(8):

        cx = now_x + dx[i]
        cy = now_y + dy[i]
        while(1):
            if (cx>=n or cy>=n or cx<0 or cy<0 or myMap[cx][cy] == 0):
                can_be_change = []
                break
            if(myMap[cx][cy]== recog):
                break
            else:
                can_be_change.append([cx,cy])
            cx += dx[i]
            cy += dy[i]

        for reverse_x,reverse_y in can_be_change:
            if(recog == 1):
                myMap[reverse_x][reverse_y] = 1
            else:
                myMap[reverse_x][reverse_y] = 2
    myMap[now_x][now_y] = recog
    return myMap

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    myMap = [[0] * n for j in range(n)]
    myMap[n//2-1][n//2-1] = 2
    myMap[n // 2][n // 2] = 2
    myMap[n // 2 - 1][n // 2] = 1
    myMap[n // 2][n // 2 - 1] = 1

    for i in range(m):
        c, r, recog = map(int,input().split())
        myMap[r-1][c-1] = recog
        myMap = update(myMap,recog,r-1,c-1)

    tmp = []
    sum1 = 0
    sum2 = 0
    for i in range(n):
        tmp +=myMap[i]
    sum1 = tmp.count(1)
    sum2 = tmp.count(2)

    print("#{} {} {}" .format(test_case,sum1, sum2))