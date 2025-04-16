n = int(input())

lucas = [2, 1]

if n == 1:
    print(1)
else:
    for i in range(2, n+1):
        l = lucas[i-1] + lucas[i-2]
        lucas.append(l)
        
    print(lucas[-1])
