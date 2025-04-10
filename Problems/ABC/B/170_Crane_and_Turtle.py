x, y = map(int, input().split())

flag = False

for i in range(x+1):
    j = x - i
    
    if y == i * 2 + j * 4:
        flag = True
        break
        
if flag:
    print("Yes")
else:
    print("No")
