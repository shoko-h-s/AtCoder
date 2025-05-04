s = input()

s_list = [0] * len(s)

for i in range(len(s)):
    if (s[i] == "A") or (s[i] == "C") or (s[i] == "G") or (s[i] == "T"):
        s_list[i] = 1

length = 0
l = 0
        
for s in s_list:
    if s == 1:
        l += 1
        
        if l > length:
            length = l
            
    else:
        l = 0

print(length)

