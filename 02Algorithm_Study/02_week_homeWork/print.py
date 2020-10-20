def solution(priorities, location):
    arr = []
    for i in range(len(priorities)):
        arr.append(i)
    arr_tmp = []
    while(priorities):
        if(priorities[0] == max(priorities)):
           arr_tmp.append(arr.pop(0))
           priorities.pop(0)
        else:
            tmp = priorities.pop(0)
            priorities.append(tmp)
            tmp = arr.pop(0)
            arr.append(tmp)
    result = arr_tmp.index(location)
    answer = result + 1
    return answer
