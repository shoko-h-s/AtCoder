a, b, c, k = map(int, input().split())
s, t = map(int, input().split())

price = a * s + b * t

# 団体割引の適用判定
if s + t >= k:
    price -= c * (s + t)
    
print(price)
