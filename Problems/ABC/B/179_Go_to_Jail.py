n = int(input())
d_list = [list(map(int, input().split())) for i in range(n)]

flag = False

for i in range(n-2):
    if (d_list[i][0] == d_list[i][1]) and (d_list[i+1][0] == d_list[i+1][1]) and (d_list[i+2][0] == d_list[i+2][1]):
        flag = True
        break
        
if flag:
    print("Yes")
else:
    print("No")
