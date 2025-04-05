n, m = map(int, input().split())

total = 0
flag = True

for i in range(m+1):
    total += n ** i
    
    if total > 10 ** 9:
        print("inf")
        flag = False
        break
        
if flag:
    print(total)
