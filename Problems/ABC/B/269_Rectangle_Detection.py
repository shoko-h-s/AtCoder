s_list = [input() for _ in range(10)]

start_flag = False

for i in range(10):
    if (s_list[i] != "..........") and (not start_flag):
        start_flag = True
        a = i + 1
        b = a
        c = s_list[i].index("#") + 1
        d = s_list[i].count("#") + c - 1

    elif (s_list[i] != "..........") and start_flag:
        b = i + 1

print(a, b)
print(c, d)
