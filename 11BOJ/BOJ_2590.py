#1. 색종이는 6종류
#[1,2,3,4,5,6]

paper = []

for i in range(6):
    tmp = int(input())
    for j in range(tmp):
        paper.append(i+1)
paper.sort(reverse=True)
print(paper)
from collections import deque
import copy
q =deque(paper)
myMap = [[0 for j in range(6)] for i in range(6)]
tmp = [[0 for j in range(6)] for i in range(6)]
print(myMap)
cnt = 0
while(q):
    ppp = q[0]
    ccccc = 0
    for i in range(len(myMap)):
        for j in range(len(myMap[0])):
            kkk = ppp*ppp
            for k in range(ppp):
                #print("j",j,"k",k)
                if(kkk == 0):
                    q.popleft()
                    break
                if(j+k<len(myMap[0])):
                    if(myMap[i][j + k] == 0):
                        myMap[i][j + k] = ppp
                        kkk-=1
                        ccccc+=1
            if(ccccc == 25):
                print(myMap)


    if(q):
        myMap = copy.deepcopy(myMap)
        myMap += tmp
        cnt+= 1