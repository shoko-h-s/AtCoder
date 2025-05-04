n = int(input())
a_list = [int(input()) for _ in range(n)]

# 降順ソート済の数列を準備、最大値を設定しておく
a_sorted = sorted(a_list, reverse=True)
a_max = a_sorted[0]

# 要素が最大値の場合のみ、2番目に大きな値を指定すればよい
for a in a_list:
    if a == a_max:
        print(a_sorted[1])
    else:
        print(a_max)
