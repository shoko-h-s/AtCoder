n, k = map(int, input().split())
a_list = list(map(int, input().split()))

# 平等に配られる量
sweets = k // n

# 再分配する量
k2 = k % n

# 再分配不要の場合
if k2 == 0:
    for _ in range(n):
        print(sweets)

else:
    # 1つ余分にもらえる番号をチェック
    a_sorted = sorted(a_list)
    num = a_sorted[k2-1]

    for a in a_list:
        # 番号が num 以下なら +1
        if a <= num:
            print(sweets + 1)
        else:
            print(sweets)
