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

bacode = {'112':0, '122':1, '221':2,'114':3, '231':4,'132':5, '411':6, '213':7, '312':8, '211':9}
hex_to_bin = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111',
              '8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}


def check(arr):
    if ((arr[7]+arr[5]+arr[3]+arr[1])*3 + arr[0]+arr[2]+arr[4]+arr[6]) % 10:
        return False
    return True
for test_case in range(1, T + 1):
    n,m = map(int,input().split())
    myMap = [input()[:m] for i in range(n)]
    visited = []
    answer = 0
    #print(myMap)
    for i in range(n):
        binStr = ''
        for ch in myMap[i]:
            #print("ch",ch)
            #print("hex_to_bin[ch]",hex_to_bin[ch])
            binStr += hex_to_bin[ch]
        #print("binStr", binStr)
        myMap[i] = binStr
    #print("myMap",myMap)

    result = []
    #0->1->0->1 총 3번 스위칭 된다
    for i in range(n):
        sw1 = sw2 = sw3 = 0
        if '1' not in myMap[i]:
            continue
        for j in range(m*4 -1,-1,-1):
            if sw2 ==0 and sw3 == 0 and myMap[i][j] == '1':
                #첫 1임
                sw1+=1
            elif sw1 and sw3 ==0 and myMap[i][j] == '0':
                #10
                sw2+=1
            elif sw1 and sw2 and myMap[i][j] == '1':
                #101
                sw3+=1
            elif sw3 and myMap[i][j] == '0':
                di = min(sw1,sw2,sw3)
                #print("SW",sw1,sw2,sw3)
                result.append(bacode[str(sw1//di)+str(sw2//di)+str(sw3//di)])
                sw1 = sw2 = sw3 = 0
                if(len(result)==8):
                    if result not in visited:
                        if(check(result)):
                            answer += sum(result)
                        visited.append(result)
                        #중복된거 거르려고
                        #ㅜㅜㅜ
                    result = []
    print("#{} {}".format(test_case,answer))

