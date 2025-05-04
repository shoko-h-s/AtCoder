h, w = map(int, input().split())

# 行数、列数のどちらかが 1 の場合は、移動ができない（= 1通りしかない）
if (h == 1) or (w == 1):
    print(1)

# 行数が偶数なら、ちょうど半分のマスに到達可能
elif h % 2 == 0:
    print((h * w) // 2)

else:
    # 行数が奇数の場合、h-1 行目まではちょうど半分のマスに到達可能
    count = (((h-1) * w) // 2)

    # 最終行は、奇数列の合計になる
    if w % 2 == 0:
        count += w // 2
    else:
        count += (w // 2) + 1

    print(count)
