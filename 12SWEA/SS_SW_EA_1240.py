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
import copy

for test_case in range(1, T + 1):
    
    # 수정, 검색에 용이한 dict를 사용하자
    bacode = {'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}

    n,m = map(int, input().split())
    ppp = [input() for i in range(n)]

    for i in range(n):
        if '1' in ppp[i]:
            tmp = copy.deepcopy(ppp[i])
            break
    #1이 있으면 바로 종료
    #앞에 시작하는 경우의 수가
    #01,,,,, 001,,,,,0001,,,, 세 가지 뿐이다
    #각각의 경우의 수에 대한 코드를 저장하고 그 코드를 가지고 제대로된 바코드인지 확인해보자
    sequ = copy.deepcopy(tmp[tmp.rfind('1') - 55 :tmp.rfind('1') + 1])

    #print(sequ)
    number = []
    result = 1
    #print(sequ)
    #print(sequ[1])
    #print(sequ[2])

    start = 0
    end = 6
    for i in range(8):
        #ttt = sequ[_][0][start:end + 1]
        number.append(bacode[sequ[start:end + 1]])
        start +=7
        end +=7

    #print("number",number)
    result = (int(number[0]) + int(number[2]) + int(number[4]) + int(number[6])) * 3 + (int(number[1]) + int(number[3])+int(number[5])) + int(number[7])
    if(result%10 ==0):
        answer = (int(number[0])+int(number[1])+int(number[2])+int(number[3])+int(number[4])+int(number[5])+int(number[6])+int(number[7]))
    else:
        answer = 0
    print("#{} {}".format(test_case,answer))






'''

decryption = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
              '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}


def Data_Extraction(Scanner):
    global N, M, Data
    for y in range(N):
        for x in range(M - 1, -1, -1):
            if Scanner[y][x] == '1':
                Data = Scanner[y][x - 55:x + 1]
                return Data


TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    Scanner = [input() for _ in range(N)]
    Data = ''
    Data_Extraction(Scanner)

    result = []
    start_i = 0
    end_i = 6
    for _ in range(8):
        result.append(decryption[Data[start_i:end_i + 1]])
        start_i += 7
        end_i += 7

    value = (result[0] + result[2] + result[4] + result[6]) * 3 + \
            (result[1] + result[3] + result[5]) + result[7]
    print("result",result)
    if not value % 10:
        print('#%d %d' % (tc, sum(result)))
    else:
        print('#%d %d' % (tc, 0))
        '''