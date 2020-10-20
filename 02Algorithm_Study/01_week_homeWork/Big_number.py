from functools import cmp_to_key
def compare(a : str,b : str):
    return a + b > b + a


def solution(numbers):
    answer = ''
    sortList = [str(i) for i in numbers]
    
    
    sortList.sort(key=cmp_to_key(lambda x, y : 1 if x + y > y + x else -1))
    #print(sortList)
    sortList.reverse()
    #sortList = sorted(sortList,key=cmp_to_key(compare))
    #print(sortList)
    if(sortList[0] =='0'):
        answer = '0'
    else:
        for i in sortList:
            answer +=i
    
    return answer