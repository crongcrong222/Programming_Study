def solution(n, lost, reserve):
    answer = 0
    che = [1] * (n)
    for i in reserve:
        che[i-1] += 1
    for i in lost:
        che[i-1] -= 1
    print("che",che)
    
    for i in range(n):
        for j in [-1,1]:
            ran = i + j
            if(ran<0 or ran >= n):
                continue;
            else:
                if(che[i] == 2 and che[ran] == 0):
                    che[i] -= 1
                    che[ran] += 1
    print("che",che)
    for i in che:
        if(i>0):
            answer += 1
            
    print("answer", answer)
    return answer
