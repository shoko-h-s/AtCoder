n = int(input())
s_list = [input() for _ in range(n)]

if s_list.count("For") > s_list.count("Against"):
    print("Yes")
else:
    print("No")
