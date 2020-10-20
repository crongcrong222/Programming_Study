
n,c = map(int,input().split())

#각 집들을 정렬하여 최대 최소 거리의 중간 값 찾기

myMap = []
for i in range(5):
    myMap.append(int(input()))

myMap.sort()

mmin = myMap[1] - myMap[0]
mmax = myMap[-1] - myMap[0]

answer = 0


while (mmin <= mmax):
    mid = (mmin + mmax) // 2
    old = myMap[0]
    count = 1

    for i in range(1, len(myMap)):
        if myMap[i] >= old + mid:
            count += 1
            old = myMap[i]

    if count >= c:
        mmin = mid + 1
        answer = mid
    else:
        mmax = mid - 1

print(answer)

'''

a = [ [1,2,3],[4,5,6]]
b = [[0] * len(a[0]) for i in range(len(a))]
for r in range(len(a)):
	for c in range(len(a[0])):
		b[len(a)-1-len(b)-1 -c][len(a[0])-r-1] = a[r][c]

for i in range(3):
	for j in range(3):
		print(b[i][j], end = ' ')
	print()
	'''