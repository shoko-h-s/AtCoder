a, b, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
xyc_list = [list(map(int, input().split())) for _ in range(m)]

# 割引券を使わない場合の最小値を求める
min_price = min(a_list) + min(b_list)

for xyc in xyc_list:
    x = xyc[0]
    y = xyc[1]
    c = xyc[2]
    price = a_list[x-1] + b_list[y-1] - c
    
    if price < min_price:
        min_price = price
        
print(min_price)
