


#1. 태욱이가 가장 왼쪽의 카드를 가져옴 pop(0)
#2. 태욱이가 가지고 있는 카드의 가장 왼쪽 또는 가장 오른쪽에 둘 수 있음
#3. 모든 카드를 다 가져온 후, 자기 앞에 놓인 카드를 순서대로 이어 붙여 문자열을 만듬
from itertools import permutations
from collections import deque
'''def dfs(cards, car,sel_card,direction):
    car.append(sel_card)
    if(direction == 1):
        car.append(sel_card)
    else:
        car.insert(0,sel_card)
    if(len(cards) == len(car)):
        return
    for j in range(1,len(cards)):
        sel_card = cards[j]
        dfs(cards,car,sel_card, 1)
        dfs(cards, car, sel_card, 0)
'''
t = int(input())
for i in range(t):
    n = int(input())
    cards = list((input().split()))
    makeCard = cards.pop(0)
    for k in cards:
        if(makeCard[0]<k):
            makeCard+=k
        elif(makeCard[0]>=k):
            makeCard = k + makeCard
    print(makeCard)