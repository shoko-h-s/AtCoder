k, s = map(int, input().split())

count = 0

for x in range(s+1):
    for y in range(s+1):
        z = s - x - y
        
        if (x <= k) and (y <= k) and (z <= k):
            if (x >= 0) and (y >= 0) and (z >= 0):
                count += 1
            
print(count)
