n = int(input())


from bisect import bisect_left,insort_left
tree = [0,300001]
answer = 0
lenarr = [-1,-1]
#초기 위치를 -1로 설정
for i in range(n):
    num = int(input())
    idx = bisect_left(tree,num)
    #넣어야 하는 위치 찾음

    c = max(lenarr[idx-1] , lenarr[idx]) + 1
    
    #넣어야 하는 위치만큼 이동을 해야 함
    #자신이 넣을 위치의 왼쪽 오른쪽 중 가장 깊이가 깊은 곳을 선택해야 바뀔 일이 없음?
    # +1을 하는 이유는 위치를 찾고 insert를 해주기 때문에
    insort_left(tree,num)
    answer +=c
    print("idx",idx)
    print("lenarr[idx-1]",lenarr[idx-1],"lenarr[idx]",lenarr[idx])
    lenarr.insert(idx,c)
    print("lenarr",lenarr)
    print("num", num)
    print(tree)
    print("c",c,"answer",answer)
    print()

