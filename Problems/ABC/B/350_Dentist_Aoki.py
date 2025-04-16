n, q = map(int, input().split())
t_list = list(map(int, input().split()))

teeth = [1 for _ in range(n)]

for t in t_list:
    if teeth[t-1] == 1:
        teeth[t-1] = 0
    else:
        teeth[t-1] = 1
        
print(sum(teeth))
