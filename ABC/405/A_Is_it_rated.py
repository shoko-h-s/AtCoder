r, x = map(int, input().split())

flag_rated = False

if x == 1:
    if 1600 <= r <= 2999:
        flag_rated = True
else:
    if 1200 <= r <= 2399:
        flag_rated = True

if flag_rated:
    print("Yes")
else:
    print("No")
