a, b = map(int, input().split())

# 先に合計を求めた方が、切り上げ除算しやすい
total = a + b

print((total + 2 - 1) // 2)
