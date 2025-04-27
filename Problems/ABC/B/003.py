s = input()
t = input()

check_set = {"a", "t", "c", "o", "d", "e", "r"}

win_flag = True

for i in range(len(s)):
    if s[i] != t[i]:
        if (s[i] == "@") and (t[i] == "@"):
            pass
        elif s[i] == "@":
            if t[i] not in check_set:
                win_flag = False
                break
        elif t[i] == "@":
            if s[i] not in check_set:
                win_flag = False
                break
        else:
            win_flag = False
            break
                
if win_flag:
    print("You can win")
else:
    print("You will lose")
