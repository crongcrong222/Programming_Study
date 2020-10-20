def solution(bridge_length, weight, truck_weights):
    answer = 0
    currentWeight = 0
    idx = 0
    bridge = []
    while(1):
        if(idx == len(truck_weights)):
            answer +=bridge_length
            break
        answer +=1
        tmp = truck_weights[idx]
        if(len(bridge) == bridge_length):
            currentWeight -=bridge[0]
            bridge.pop(0)
        if(tmp + currentWeight <= weight):
            bridge.append(tmp)
            currentWeight += tmp
            idx+=1
        else:
            bridge.append(0)

    return answer
