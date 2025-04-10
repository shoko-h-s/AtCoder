n, m = map(int, input().split())
a_list = list(map(int, input().split()))
x_list = [list(map(int, input().split())) for _ in range(n)]

flag = True

for i in range(m):
    total = 0
    
    for j in range(n):
        total += x_list[j][i]
        
    if total < a_list[i]:
        flag = False
        break
        
if flag:
    print("Yes")
else:
    print("No")
