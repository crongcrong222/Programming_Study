n, m = map(int,input().split())

myMap = [list(map(int,input().split())) for i in range(n)]

virus = []
for i in range(n):
    for j in range(n):
        if myMap[i][j] == 2 :
            virus.append([i,j])

dy = [-1,0,1,0]
dx = [0,1,0,-1]
for y,x in virus:
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if myMap[ny][nx] == 0:
                print(ny,nx)
                myMap[ny][nx] = 1
total = 0
for i in myMap:
    total += i.count(0)
print(total)

for i in range(n):
    for j in range(n):
        print(myMap[i][j], end = ' ')
    print()