y = int(input())

flag = False

if y % 400 == 0:
    flag = True
elif y % 100 == 0:
    pass
elif y % 4 == 0:
    flag = True
    
if flag:
    print("YES")
else:
    print("NO")
