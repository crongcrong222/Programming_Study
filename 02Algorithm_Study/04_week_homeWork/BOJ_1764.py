a,b = map(int, input().split())


d = {}
for i in range(a + b):
    tmp = input()
    if( tmp in d):
        d[tmp] +=1
    else:
        d[tmp] = 1

answer = []
for k,v in d.items():
    if(v == 2):
        answer.append(k)

answer.sort()
print(len(answer))
for i in answer:
    print(i)


