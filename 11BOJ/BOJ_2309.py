from itertools import combinations

nan = [int(input()) for i in range(9)]

nan.sort()

hubo = list(combinations(nan,7))
for i in hubo:
    if(sum(i) == 100):
        answer = i
        break
for i in answer:
    print(i)