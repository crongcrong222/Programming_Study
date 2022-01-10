def solution(n, k, cmd):
    aaa = ''
    answer = ['O' for i in range(8)]
    del_position_stack = []
    present_position = k + 1
    
    # 딕셔너리의 주요 시간 복잡도는 O(1)이기 때문에 효율성 문제에서 딕셔너리를 사용하여 문제를 풀어야 함
    
    my_linked_list = {i : [i-1, i+1] for i in range(1,n+1)}
    for order in cmd:
        if (len(order) > 1):
            if(order[0] == 'D'):
                for i in range(int(order[-1])):
                    present_position = my_linked_list[present_position][1]

            else:
                for i in range(int(order[-1])):
                    present_position = my_linked_list[present_position][0]
                
        else:
            if (order[0] == 'C'):
                prev, next = my_linked_list[present_position]
                del_position_stack.append([prev, present_position, next])
                answer[present_position - 1] = 'X'
                
                if (next == n + 1):
                    present_position = my_linked_list[present_position][0]
                else:
                    present_position = my_linked_list[present_position][1]
                
                #맨 처음 부분 삭제시
                if (prev == 0):
                    my_linked_list[next][0] = 0
                
                #가장 마지막 부분 삭제시
                elif (next == n + 1):
                    my_linked_list[prev][1] = n + 1
                else:
                    my_linked_list[prev][1] = next
                    my_linked_list[next][0] = prev
            
            elif (order[0] == 'Z'):
                prev, present, next = del_position_stack.pop()
                answer[present - 1] = 'O'
                
                if (prev == 0):
                    my_linked_list[next][0] = present
                elif (next == n + 1):
                    my_linked_list[prev][1] = present
                else:
                    my_linked_list[prev][1] = present
                    my_linked_list[next][0] = present
    for i in answer:
        aaa+= i
    return aaa
