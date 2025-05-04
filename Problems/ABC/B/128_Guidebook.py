n = int(input())
sp_list = [input().split() for _ in range(n)]

# ソート済と照らし合わせるリストを作成
sp_list_2 = []

for sp in sp_list:
    sp2 = [sp[0], int(sp[1])]
    sp_list_2.append(sp2)

# 降順を優先して、2回ソートする
sp_sorted = sorted(sp_list_2, key=lambda x: x[1], reverse=True)
sp_sorted = sorted(sp_sorted, key=lambda x: x[0])

for sp in sp_sorted:
    print(sp_list_2.index(sp) + 1)
