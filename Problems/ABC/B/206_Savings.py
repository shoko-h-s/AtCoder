n = int(input())

i = 1
bank = 0

while bank < n:
    bank += i
    
    if bank < n:
        i += 1
    
print(i)
