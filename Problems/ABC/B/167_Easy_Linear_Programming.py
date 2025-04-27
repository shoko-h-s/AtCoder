a, b, c, k = map(int, input().split())

total = 0

if a >= k:
    total = k
else:
    total += a
    k -= a
    
    if b < k:
        k -= b
        total -= k
        
print(total)
