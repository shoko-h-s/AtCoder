q, h, s, d = map(int, input().split())
n = int(input())

# 0.5l の最安値
buy_05 = min(h, q*2)

# 1l の最安値
buy_1 = min(s, buy_05*2)

# 2l の最安値
buy_2 = min(d, buy_1*2)

if n % 2 == 0:
    price = buy_2 * (n // 2)

else:
    price = buy_2 * (n // 2)
    price += buy_1

print(price)
