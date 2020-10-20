def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        startIn = commands[i][0] - 1
        endIn = commands[i][1]
        tmpList = array[startIn:endIn]
        tmpList = sorted(tmpList)
        returnIn = commands[i][2] - 1
        answer.append(tmpList[returnIn])
    return answer
