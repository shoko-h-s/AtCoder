n = int(input())
s = input()

string = ""

for i in range(len(s)):
    change = ord(s[i]) + n
    
    # chr(90) = Z
    if change > 90:
        change -= 26
        
    string += chr(change)
    
print(string)
