s = input()

display = ""

for i in range(len(s)):
    if s[i] == "0":
        display += "0"
    elif s[i] == "1":
        display += "1"
    else:
        display = display[:-1]
        
print(display)
