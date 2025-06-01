s = input()

flag = True

for i in range(len(s)):
    if (i % 2 == 1) and (s[i] != "0"):
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
