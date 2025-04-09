n, m = map(int, input().split())
h_list = list(map(int, input().split()))

success_flag = True

for i in range(n):
    if m >= h_list[i]:
        m -= h_list[i]
    
    else:
        print(i)
        success_flag = False
        break
        
if success_flag:
    print(n)
