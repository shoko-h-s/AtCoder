n, t = map(int, input().split())
c_list = list(map(int, input().split()))
r_list = list(map(int, input().split()))

max_num = 0

if t in c_list:
    for i in range(n):
        if (c_list[i] == t) and (r_list[i] > max_num):
            max_num = r_list[i]
            player = i+1
            
else:
    color = c_list[0]
    max_num = r_list[0]
    player = 1
    
    for i in range(1, n):
        if (c_list[i] == color) and (r_list[i] > max_num):
            max_num = r_list[i]
            player = i+1
            
print(player)
