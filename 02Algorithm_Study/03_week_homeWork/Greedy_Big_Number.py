def solution(number,k):

    answer = [number[0]]

    for num in number[1:]:
        while len(answer)>0 and answer[-1]<num and k>0:
            k-=1
            answer.pop()
        answer.append(num)
    if(k!=0):
        answer = answer[:-k]


    answer = ''.join(answer)
        
    
    return answer

#https://jjluveeecom.tistory.com/10
print(solution("4177252841",4))
        
                
                
