import collections
def solution(genres, plays):
    answer = []
    pdic = {}
    dic = {}
    summ = 0
    for i in range(len(genres)):
        pdic[genres[i]] = pdic.get(genres[i],0) + plays[i]
        dic[genres[i]] = dic.get(genres[i],[]) + [(plays[i],i)]

    pdic_sort = sorted(pdic.items(), key = lambda x : x[1] , reverse = True)

    for(genre, allplay) in pdic_sort:
        dic[genre] = sorted(dic[genre], key = lambda x:(-x[0], x[1]))
        answer += [i for (play,i) in dic[genre][:2]]

    return answer
