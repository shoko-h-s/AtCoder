import math

n = int(input())

# 階乗を求める
power = math.factorial(n)

print(power % (10**9 + 7))
