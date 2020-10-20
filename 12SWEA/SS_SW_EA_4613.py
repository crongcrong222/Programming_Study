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

#import sys


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

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.


#https://mungto.tistory.com/246


git = ['W','B','R']
def init():
    global result
    #러시아 국기이기 때문에 맨 위에 1줄은 무조건 W이고 맨 아래 무조건 R임
    result += myMap[0].count("B")
    result += myMap[0].count("R")
    result += myMap[r-1].count("W")
    result += myMap[r-1].count("B")


def dfs(idx, color, total):
    global result
    #불필요 한 것 가지치기
    #total이 result보다 크면 필요가 없기 때문에 가지치기
    if(result <= total):
        return
    #r번째까지 idx를 다 봤으면 결과 더하기
    if(idx >= r-1):
        result = total
        return
    for i in range(color,3):
        tmp = 0
        #마지막 줄까지 왔는데 국기 하얀색이라면 필요가 없기 때문에 넘긴다
        if( idx >= r -2 and i == 0):
            continue
        for j in myMap[idx]:
            #현재 줄에서 내가 선택한 색상가 다른 걸 카운트(이게 적어야 함)
            #적은 지 많은 지 파악하는건 가장 위에 가지치기
            if(j != git[i]):
                tmp +=1
        #dfs로 다음 줄로 진행
        dfs(idx+1,i, total+tmp)




for test_case in range(1, T + 1):
    r, c = map(int,input().split())
    #각 줄의 W,B,R의 갯수 저장하는 리스트 생성
    #각 줄 중 가장 많은 것 부터 색칠하기
    myMap = [list(input()) for i in range(r)]
    INF = 1e9
    result = INF
    dfs(1,0,0)
    init()

    print('#{} {}'.format(test_case,result))


