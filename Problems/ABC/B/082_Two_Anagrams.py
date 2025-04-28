s_list = list(input())
t_list = list(input())

s_sorted = sorted(s_list)
t_sorted = sorted(t_list, reverse=True)

s_dash = "".join(s_sorted)
t_dash = "".join(t_sorted)

if s_dash < t_dash:
    print("Yes")
else:
    print("No")
