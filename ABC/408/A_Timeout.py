n, s = map(int, input().split())
t_list = list(map(int, input().split()))

flag = True

for i in range(n):
    if i == 0:
        if t_list[i] > s:
            flag = False
            break

    else:
        if t_list[i] - t_list[i-1] > s:
            flag = False
            break

if flag:
    print("Yes")
else:
    print("No")
