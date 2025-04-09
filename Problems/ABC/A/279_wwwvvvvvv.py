s = input()

total = 0

for i in range(len(s)):
    if s[i] == "v":
        total += 1
    else:
        total += 2
        
print(total)
