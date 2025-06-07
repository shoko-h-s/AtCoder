s = input()

max_s = 0

for i in range(len(s)):
    for j in range(i, len(s)):
        s_ij = s[i:j+1]
        
        if s_ij == s_ij[::-1]:
            max_s = max(max_s, len(s_ij))

print(max_s)
