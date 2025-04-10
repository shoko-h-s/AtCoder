n, d = map(int, input().split())
t_list = list(map(int, input().split()))

flag = False

for i in range(n-1):
    if t_list[i+1] - t_list[i] <= d:
        flag = True
        print(t_list[i+1])
        break
        
if not flag:
    print(-1)
