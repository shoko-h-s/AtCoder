n, s, d = map(int, input().split())
xy_list = [list(map(int, input().split())) for i in range(n)]

flag = False

for xy in xy_list:
    if (xy[0] < s) and (xy[1] > d):
        flag = True
        break
        
if flag:
    print("Yes")
else:
    print("No")
