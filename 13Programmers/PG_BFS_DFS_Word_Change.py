def dfs(begin, target, words,visited):
    answer = 0
    stack = [begin]
    while(stack):
        tmp = stack.pop()
        if(tmp == target):
            print("answer",answer)
            return answer
        for j in range(len(words)):
            count = 0
            for i in range(len(begin)):
                if(tmp[i] !=words[j][i]):
                    count +=1
            print(count)
            if(count == 1):
                #한 번에 한 개의 알파벳만 바꿀 수 있음
                if(visited[j] != 0):
                    continue
                visited[j] = 1
                stack.append(words[j])
                #한 개의 알파벳만 다른 단어들 후보를 다 스택에 추가
        answer+=1
def solution(begin, target, words):
    answer = 0
    q = []
    visited = [0 for i in range(len(words))]

    if not (target in words):
        return 0
    else:
        answer = dfs(begin, target, words,visited)

    return answer
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
