H, W = map(int, input().split())
h, w = map(int, input().split())

cols = h * W
lines = w * H

# 列・行の重複部分
dupli = h * w

# 塗られたマス
blacks = cols + lines - dupli

print(H * W - blacks)
