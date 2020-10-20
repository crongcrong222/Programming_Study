'''from collections import Counter

t=int(input())
n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int,input().split()))

def toPointer(lst,l):
  r=[]
  for i in range(l):
    temp=0
    for j in range(i,l):
      temp += lst[j]
      r.append(temp)
  return r

al = toPointer(a,n)
bl = toPointer(b,m)
print("al",al)
print("bl",bl)
result = 0
c=Counter(bl)
print("C",c)
for i in al:
  result+=c[t-i]
  print("t-i",t-i)
  print("c[t-i]",c[t-i])
  print("resut",result)

print(result) 
'''
import sys
from collections import Counter


def sumAllList(sumList,n):
    tmp = []
    for i in range(len(sumList)):
        Ntmp = 0
        for j in range(i,len(sumList)):
            Ntmp +=sumList[j]
            tmp.append(Ntmp)
        #if(tmp[-1]>=n):
        #    tmp.pop()
    return tmp

n = int(sys.stdin.readline().rstrip())

aN = int(sys.stdin.readline().rstrip())


a = list(map(int,sys.stdin.readline().rstrip().split()))

bN = int(sys.stdin.readline().rstrip())


b = list(map(int,sys.stdin.readline().rstrip().split()))


a = sumAllList(a,n)

b = sumAllList(b,n)

'''
count = [0] * (aN+bN)

for i in range(len(b)):
    count[b[i]] +=1

result = 0

for i in range(len(a)):
    tmp = n - a[i]
    if(n>0):
        result += count[tmp]
    

print(result)'''


sum = 0

col = Counter(b)

for i in a:
    sum += col[n-i]

print(sum)

