n, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

flag = True

for b in b_list:
    if b in a_list:
        a_list.remove(b)
        
    else:
        flag = False
        break
        
if flag:
    print("Yes")
else:
    print("No")
