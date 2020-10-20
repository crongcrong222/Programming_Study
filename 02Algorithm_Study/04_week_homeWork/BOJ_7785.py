cnt = int(input())




dic = {}

for i in range(cnt):
    name, status = map(str, input().split())
    if(status == "leave"):
            dic[name] = 0

    elif(status == "enter"):
            dic[name] = 1

answer = []
for k,v in dic.items():
    if(v == 1):
        answer.append(k)
answer.sort(reverse = True)


for i in answer:
    print(i)
