x, y = map(int, input().split())

# 必要な残額
rest = y - x

if rest <= 0:
    print(0)
else:
    print((rest + 10 - 1) // 10)
