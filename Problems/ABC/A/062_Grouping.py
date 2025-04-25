set_1 = {1, 3, 5, 7, 8, 10, 12}
set_2 = {4, 6, 9, 11}

xy_set = set(map(int, input().split()))

# x, y が、どちらかのグループの部分集合かどうか調べる
if (xy_set <= set_1) or (xy_set <= set_2):
    print("Yes")
else:
    print("No")
