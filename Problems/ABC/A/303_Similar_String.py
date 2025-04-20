n = int(input())
s = input()
t = input()

flag = True

# 条件を満たしているときは pass にする方が実装しやすい
for i in range(n):
    if s[i] == t[i]:
        pass
    elif (s[i] == "1" and t[i] == "l") or (s[i] == "l" and t[i] == "1"):
        pass
    elif (s[i] == "0" and t[i] == "o") or (s[i] == "o" and t[i] == "0"):
        pass
    else:
        flag = False
        break
        
if flag:
    print("Yes")
else:
    print("No")
