a, b, c, d = map(int, input().split())

minute_t = 60 * a + b
minute_a = 60 * c + d

if minute_t <= minute_a:
    print("Takahashi")
else:
    print("Aoki")
