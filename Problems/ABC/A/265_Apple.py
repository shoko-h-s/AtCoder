x, y, n = map(int, input().split())

price = 0

mod_3 = n % 3

# mod 3 の部分は、1 個ずつ買う必要がある
if mod_3 != 0:
    price += mod_3 * x
    n -= mod_3

# 1 個当たりの単価が安い方で、残りの個数を購入する
if x * 3 >= y:
    price += y * (n // 3)
else:
    price += x * n
    
print(price)
