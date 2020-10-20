
h, w = map(int, input().split())

cut = int(input())
h_max = 0
w_max = 0
h_list = [0]
w_list = [0]

for i in range(cut):
    cuttt = input().split()

    if cuttt[0] == '1':
        h_list.append(int(cuttt[1]))
    else:
        w_list.append(int(cuttt[1]))
h_list = sorted(h_list)
w_list = sorted(w_list)

h_list.append(h)
w_list.append(w)

for i in range(len(h_list)-1):
    if(h_max< h_list[i + 1] - h_list[i]):
       h_max = h_list[i + 1] - h_list[i]

for i in range(len(w_list)-1):
    if(w_max< w_list[i + 1] - w_list[i]):
       w_max = w_list[i + 1] - w_list[i]

print(h_max*w_max)
