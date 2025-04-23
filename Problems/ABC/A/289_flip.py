s = input()

s_new = ""

for i in range(len(s)):
    if s[i] == "0":
        s_new += "1"
    else:
        s_new += "0"
        
print(s_new)
