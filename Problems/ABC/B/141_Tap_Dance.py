s = input()

flag = True

# R, L の時だけ判定すればよい
for i in range(len(s)):
    if (s[i] == "L") and (i % 2 == 0):
        flag = False
        break
        
    elif (s[i] == "R") and (i % 2 == 1):
        flag = False
        break
        
if flag:
    print("Yes")
else:
    print("No")
