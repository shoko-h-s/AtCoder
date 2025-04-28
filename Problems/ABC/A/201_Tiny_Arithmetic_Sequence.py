a_list = list(map(int, input().split()))

# 昇順ソートを行えば判定可能になる
a_sorted = sorted(a_list)

if a_sorted[2] - a_sorted[1] == a_sorted[1] - a_sorted[0]:
    print("Yes")
else:
    print("No")
