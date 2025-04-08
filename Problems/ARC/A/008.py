n = int(input())

# 10 で割った余りが 6 以下なら、端数は 1個ずつ買った方が安い
rest = n % 10

if rest <= 6:
    packs = n // 10
    print(packs * 100 + rest * 15)
    
else:
    packs = n // 10 + 1
    print(packs * 100)
