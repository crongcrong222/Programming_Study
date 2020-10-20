from bisect import bisect


def solution(length, port):

    d = [port[0]]
    for i in range(1, length):
        if d[-1] < port[i]:
            d.append(port[i])
        else:
            d[bisect(d,port[i])] = port[i]
              
    return len(d)
            
# https://ioqoo.tistory.com/14 참

n = int(input())
port = list(map(int,input().split()))
print(solution(n,port))
