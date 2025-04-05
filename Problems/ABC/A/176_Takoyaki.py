import math

n, x, t = map(int, input().split())

# 作る回数を求める
num = math.ceil(n / x)

print(t * num)
