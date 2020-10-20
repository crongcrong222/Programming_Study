from collections import defaultdict



def ssa(n,trust):
    ddd =defaultdict(list)
    for i in trust:
        ddd[i[1]].append(i[0])

    judge = []
    for i in range(n):
        if(len(ddd[i+1]) == n-1):
            judge.append(i+1)

    if(len(judge) != 1):
        return -1
    for i in trust:
        if(i[0] == judge[0]):
            return -1
    return judge[0]
            
        
n = 4

trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]

print(ssa(n,trust))
