abc_list = list(map(int, input().split()))

abc_sorted = sorted(abc_list)

# 最も多いパックの個数が、他 2 つの個数合計と等しくなれば良い
if abc_sorted[0] + abc_sorted[1] == abc_sorted [2]:
    print("Yes")
else:
    print("No")
