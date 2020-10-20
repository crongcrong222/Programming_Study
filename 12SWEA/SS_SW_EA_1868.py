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
dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]


def checkArr(arr, aroundPos):

    while aroundPos:
        x,y = aroundPos.pop(0)

        count  = 0
        temp_around  = []

        if arr[x][y] != '.':
            continue
        # .이 아니면 폭탄이거나, 카운트 된 자리임
        for i in range(8):
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            if temp_x >= 0 and temp_y >= 0 and temp_x < n and temp_y < n:
                a=arr[temp_x][temp_y]
                if (a == '*'):
                    count  += 1
                elif (a == '.'):
                    temp_around.append([temp_x, temp_y])
        arr[x][y] = count
        if count  == 0 :
        #만약 popingcnt가 0이면 주변에 지뢰가 없는 위치이다
        #이 경우에만 주변을 다시 탐색하기 위해 positionList에 추가한다
            aroundPos += temp_around
            

'''def checkArr(arr, aroundPos):
    """
    Count the number of bomb, while pushing positions around pos
    if it is bomb, don't explore anymore
    """
    dx = [1, -1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, 1, -1, -1, 1, -1, 1]

    while aroundPos:
        # pos that needs to be checked around
        x,y = aroundPos.pop(0)
        count = 0
        temp_around = []

        # only normal position
        if arr[x][y] != '.':
            continue

        for i in range(8):
            temp_x = x + dx[i]
            temp_y = y + dy[i]

            if temp_x >= 0 and temp_y >= 0 and temp_x < n and temp_y < n:
                value = arr[temp_x][temp_y]
                if value == "*":
                    count += 1
                elif value == ".":
                    temp_around.append((temp_x,temp_y))
        arr[x][y] = count
        # check temp_around if the is no bomb around pos
        if count == 0:
            aroundPos += temp_around
            
            '''
def solve(arr,n):
    clickcnt = 0

    for i in range(n*n):
        ifpop = False
        x,y = i//n,i%n
        if(arr[x][y] != '.'):
            continue
        positionList = []
        for dir in range(8):
            cx = x + dx[dir]
            cy = y + dy[dir]
            if(cx>=n or cy>=n or cx<0 or cy<0):
                continue
            else:
                if (arr[cx][cy] == '*'):
                    ifpop = True
                    break
                else:
                    positionList.append([cx, cy])
        if(ifpop):
            continue
        #하나라도 폭탄이 있으면 continue
        clickcnt+=1
        arr[x][y] = 0
        #폭탄이 하나도 없는 경우 체크
        #그 이후 한 개라도 있으면 그 다음 체크
        checkArr(arr,positionList)
    for i in range(n*n):
        x,y = i//n,i%n
        if(arr[x][y] =='.'):
            #하나라도 체크하지 않은 부분이 있으면 cnt
            clickcnt+=1
    return clickcnt




for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(input().strip()) for i in range(n)]

    answer = solve(arr,n)
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()
    print("#{} {}" .format(test_case, answer))