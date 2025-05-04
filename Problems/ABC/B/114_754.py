s = input()

min_num = 753

for i in range(len(s)-2):
    x = int(s[i:i+3])
    d = abs(x - 753)
    
    if d < min_num:
        min_num = d
        
print(min_num)
