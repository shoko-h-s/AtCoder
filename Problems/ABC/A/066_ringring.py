price_list = list(map(int, input().split()))

# 合計から最高値を引いたものが答え
print(sum(price_list) - max(price_list))
