n = int(input())
p_list = [int(input()) for _ in range(n)]

# 最も高い商品を抽出
max_price = max(p_list)

price = (max_price // 2) + sum(p_list) - max_price

print(price)
