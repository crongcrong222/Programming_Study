from itertools import permutations

def solution(k, dungeons):
    len_arr = len(dungeons)
    
    permutations_list = list(permutations(dungeons, len_arr))
    
    answer_list = []
    
    for i in range(len(permutations_list)):
        init_fatigue = k
        tmp_dungeons = permutations_list[i]
        answer = 0
        for j in range(len_arr):
            need_fatigue = tmp_dungeons[j][0]
            spend_fatigue = tmp_dungeons[j][1]
            if(init_fatigue >= need_fatigue):
                answer+=1
                init_fatigue -= spend_fatigue
        answer_list.append(answer)
    answer_list.sort()

    return answer_list[-1]