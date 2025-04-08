n, d = map(int, input().split())

# 1人当たりが監視できる数
trees = 2 * d + 1

print((n + trees - 1) // trees)
