def solution(name):
    answer = 0
    tmp = ['A'] * len(name)
    name=list(name)

    i = 0
    
    while(1):
        tmp[i] = name[i]
        if(ord(name[i]) - ord('A') > ord('Z') + 1 - ord(name[i])):
            answer =answer + ord('Z') + 1 -  ord(name[i])
        else:
            answer =answer+ ord(name[i]) - ord('A')
        if(tmp == name):
            break
        for move in range(1,len(name)):
            if(name[ ( i + move) % len(name)] != tmp[(i + move) % len(name)]):
                i = (i + move)%len(name)
                answer +=move
                break;
            elif(name[(i + len(name)-move)%len(name)] != tmp[(i+len(name)-move)%len(name)]):
                 i = (i + len(name) -move)%len(name)
                 answer +=move
                 break;
        
    return answer


print(solution("JAN"))
