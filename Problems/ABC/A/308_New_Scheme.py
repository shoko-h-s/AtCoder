s_list = list(map(int, input().split()))

flag = True

for i in range(7):
    
    # 広義単調増加は = を含む
    if s_list[i] > s_list[i+1]:
        flag = False
        break
        
if flag:
    if (s_list[0] < 99) or (s_list[-1] > 675):
        flag = False
        
    else:
        s25_list = [s for s in s_list if s % 25 == 0]
        
        if len(s25_list) < 8:
            flag = False
            
if flag:
    print("Yes")
else:
    print("No")
