n, h, x = map(int, input().split())
p_list = list(map(int, input().split()))

for i in range(n):
    power = h + p_list[i]
    
    if power >= x:        
        print(i+1)
        break
