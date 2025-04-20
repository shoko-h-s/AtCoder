n = int(input())
apx_list = [input() for _ in range(n)]

min_price = 10**9 + 1
flag = False

for apx in apx_list:
    a, p, x = map(int, apx.split())
    
    if a < x:
        min_price = min(p, min_price)
        flag = True
        
if flag:
    print(min_price)
else:
    print(-1)
