n, m, a, b = map(int, input().split())
c_list = [int(input()) for _ in range(m)]

flag = True

for i in range(m):
    if n <= a:
        n += b    
    
    if n >= c_list[i]:
        n -= c_list[i]
        
    else:
        print(i+1)
        flag = False
        break
        
if flag:
    print("complete")
