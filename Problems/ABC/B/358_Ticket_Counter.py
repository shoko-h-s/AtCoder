n, a = map(int, input().split())
t_list = list(map(int, input().split()))

x_list = [0]

for i in range(n):
    x = max(x_list[i], t_list[i]) + a
    print(x)
    x_list.append(x)
