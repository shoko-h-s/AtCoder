s = input()

str_list = [0, 0, 0, 0, 0, 0]

for i in range(len(s)):
    if s[i] == "A":
        str_list[0] += 1
    elif s[i] == "B":
        str_list[1] += 1
    elif s[i] == "C":
        str_list[2] += 1
    elif s[i] == "D":
        str_list[3] += 1
    elif s[i] == "E":
        str_list[4] += 1
    else:
        str_list[5] += 1
        
print(*str_list)
