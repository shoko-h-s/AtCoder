n, m, p = map(int, input().split())

day = 1
count = 0
i = 0

while day <= n:
    if day == m + p * i:
        count += 1
        i += 1
        
    day += 1
    
print(count)
