n = int(input())
xu_list = [input().split() for _ in range(n)]

total = 0

for xu in xu_list:
    x = float(xu[0])
    u = xu[1]
    
    if u == "BTC":
        total += 380000.0 * x
    else:
        total += x
        
print(total)
