n = int(input())
s_list = [input() for _ in range(n)]

flag = False

for i in range(n):
    for j in range(n):
        if i == j:
            pass
        
        else:
            t = s_list[i] + s_list[j]
            
            if t == t[::-1]:
                flag = True
                break
                
if flag:
    print("Yes")
else:
    print("No")
