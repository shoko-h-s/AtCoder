n, y = map(int, input().split())

flag = False

for i in range(n+1):
    for j in range(n-i+1):
        k = n - i - j
        
        if y == 10000 * i + 5000 * j + 1000 * k:
            print(i, j, k)
            flag = True
            break
            
    if flag:
        break
        
if not flag:
    print(-1, -1, -1)
