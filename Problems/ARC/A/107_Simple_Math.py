a, b, c = map(int, input().split())

# 1次式の和の公式
a_total = (a * (a+1)) // 2
b_total = (b * (b+1)) // 2
c_total = (c * (c+1)) // 2

total = a_total * b_total * c_total

print(total % 998244353)
