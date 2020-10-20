import collections

def solution(clothes):
    answer = 1
    dic = dict()
    for i in range(len(clothes)):
        k = clothes[i][1]
        v = clothes[i][0]
        if( k in dic):
            dic[k].append(v)
        else:
            dic[k] = [v]

    
    for i in dic.keys():
        answer = answer * (len(dic[i]) + 1)
    return answer - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
