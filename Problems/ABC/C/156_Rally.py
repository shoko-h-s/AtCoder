n = int(input())
x_list = list(map(int, input().split()))

x_ave_1 = sum(x_list) // n
x_ave_2 = sum(x_list) // n + 1

# 偏差をリスト化する
# 平均値2パターン（切り上げ、切り捨て）でそれぞれ総和を計算 → 最小値を採用
x_var_1 = [(x - x_ave_1)**2 for x in x_list]
x_var_2 = [(x - x_ave_2)**2 for x in x_list]

x_sum_1 = sum(x_var_1)
x_sum_2 = sum(x_var_2)

print(min(x_sum_1, x_sum_2))



# 【備考】
# Training Easy 2
