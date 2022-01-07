def change_milk(before):
    if(before == 0):
        return 1
    elif(before == 1):
        return 2
    elif(before == 2):
        return 0




len_arr = int(input())
arr = list(map(int,input().split()))

next_milk = 0
answer = 0
for i in range(len_arr):
    if(next_milk == arr[i]):
        answer += 1
        next_milk = change_milk(next_milk)
        

print(answer)