def solution(numbers, target):
    total = [0]
    for i in numbers:
        tmp = []
        for j in total:
            add = j + i
            sub = j - i
            tmp.append(add)
            tmp.append(sub)
            print("add",add)
            print("sub",sub)
            print("total",total)
            print("tmp",tmp)
            print("----------------------")
        total = tmp





print(solution([1,1,1,1,1],3))
