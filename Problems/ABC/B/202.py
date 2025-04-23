s = input()

s_rev = s[::-1]
s_180 = ""

for i in range(len(s_rev)):
    if s_rev[i] == "6":
        s_180 += "9"
    elif s_rev[i] == "9":
        s_180 += "6"
    else:
        s_180 += s_rev[i]
        
print(s_180)
