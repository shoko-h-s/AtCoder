n = list(input())

flag = True

if len(n) == 1:
    print("Yes")
    
else:
    for i in range(len(n) - 1):
        if int(n[i]) <= int(n[i+1]):
            flag = False
            break
            
    if flag:
        print("Yes")
    else:
        print("No")
