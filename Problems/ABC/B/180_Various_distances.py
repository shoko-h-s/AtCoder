n = int(input())
x_list = list(map(int, input().split()))

x_abs_list = [abs(x) for x in x_list]

# マンハッタン距離
d1 = sum(x_abs_list)

# ユークリッド距離
x2_abs_list = [x**2 for x in x_abs_list]
d2 = (sum(x2_abs_list))**0.5

# チェビシェフ距離
d3 = max(x_abs_list)

print(d1)
print(d2)
print(d3)
