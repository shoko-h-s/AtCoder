n = int(input())

total = 0

for i in range(1, n+1):
    if (i % 15 != 0) and (i % 3 != 0) and (i % 5 != 0):
        total += i
        
print(total)
