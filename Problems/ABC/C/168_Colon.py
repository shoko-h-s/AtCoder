import math

a, b, h, m = map(int, input().split())

# 分針、時針の位置
now_m = m * 6
now_h = h * 30 + (m * 0.5)

# 針のなす角を求める
angle = abs(now_h - now_m)
angle = math.radians(angle)

# 余弦定理を適用
c2 = a**2 + b**2 - 2 * a * b * math.cos(angle)

print(c2 ** 0.5)
