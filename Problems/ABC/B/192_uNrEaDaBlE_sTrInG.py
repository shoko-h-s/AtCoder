s = input()

flag = True

for i in range(len(s)):
    if (i % 2 == 0) and (s[i].isupper()):
        flag = False
    elif (i % 2 == 1) and (s[i].islower()):
        flag = False
        
    if not flag:
        break
        
if flag:
    print("Yes")
else:
    print("No")
