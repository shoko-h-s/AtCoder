n, m, x, t, d = map(int, input().split())

if x <= m:
    print(t)
else:
    growth_year = x - m
    print(t - d * growth_year)
