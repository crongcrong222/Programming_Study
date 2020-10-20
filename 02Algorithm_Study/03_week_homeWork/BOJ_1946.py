import sys
def solution(length, people):
    people.sort()

    cnt = 1
    minn = people[0][1]
    for i in range(1,length):
        
        if(people[i][1] < minn):
            cnt +=1
            minn = people[i][1]
    return cnt


n = int(sys.stdin.readline().rstrip())

for j in range(n):
    a = []
    loop = int(sys.stdin.readline().rstrip())
    for i in range(loop):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        a.append([x,y])
    print(solution(loop,a))
