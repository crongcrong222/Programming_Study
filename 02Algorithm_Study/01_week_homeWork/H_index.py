def solution(citations):
    answer = 0
    h_index = len(citations)
    citations = sorted(citations,reverse = True)
    print(citations)
    while(len(citations) != 0 ):
        if(h_index<=citations[-1]):
            answer = h_index
            break;
        else:
            citations.pop()
            h_index = len(citations)
    return answer