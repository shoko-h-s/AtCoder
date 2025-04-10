n, k = map(int, input().split())
t_list = [int(input()) for _ in range(n)]

flag = True

for i in range(3, n+1):
    times = sum(t_list[i-3:i])
    
    if times < k:
        print(i)
        flag = False
        break

if flag:
    print(-1)
