x = int(input())

total = 0

# 500円、5円の順に可能な限り両替する
if x >= 500:
    coin_500 = x // 500
    total += 1000 * coin_500
    x = x % 500
    
if x >= 5:
    coin_5 = x // 5
    total += 5 * coin_5
    
print(total)
