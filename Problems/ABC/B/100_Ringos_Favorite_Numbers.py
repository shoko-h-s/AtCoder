d, n = map(int, input().split())

n_list = []
i = 1

while len(n_list) < n:
    if d == 0:
        if i % 100 != 0:
            n_list.append(i)

    elif d == 1:
        i_100 = i * 100

        if i_100 % 10000 != 0:
            n_list.append(i_100)

    else:
        i_100 = i * 10000

        if i_100 % 1000000 != 0:
            n_list.append(i_100)

    i += 1

print(n_list[-1])
