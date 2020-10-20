import collections


def solution (participant, completion):
    partiDic = collections.Counter(participant)
    com = collections.Counter(completion)
    answer = list(partiDic - com)
    return answer[0]



print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
