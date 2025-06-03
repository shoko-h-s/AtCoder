x, y, n = map(int, input().split())

div_n, mod_n = divmod(n, 3)

if y <= 3 * x:
    print(y * div_n + x * mod_n)
else:
    print(x * n)
