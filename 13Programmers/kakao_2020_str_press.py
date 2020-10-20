def solution(s):
    answer = len(s)
    
    for i in range( 1, len(s)//2 + 1):
        result = ""
        tmp = s[0:i]
        print("tmp",tmp)
        count = 1
        for j in range(i,len(s) + 1,i):
            if(tmp == s[j:j+i]):
                count +=1
                print("ASDASD")

            else:
                if(count == 1):
                    result += tmp
                else:
                    result= result + str(count) + tmp
                    

                tmp = s[j:j+i]
                count = 1
            print("result",result)    
        result += s[(len(s)//i)*i:]
        #print("s[(len(s)//i)*i:]",s[(len(s)//i)*i:])
        print("---------result",result)
        answer = min(answer, len(result))
    return answer



print(solution("abcabcabcabcdededededede"))
