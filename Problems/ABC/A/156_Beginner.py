# 156_Beginner

n, r = map(int, input().split())

if n >= 10:
    print(r)
else:
    cor = 100 * (10 - n)
    print(r + cor)
