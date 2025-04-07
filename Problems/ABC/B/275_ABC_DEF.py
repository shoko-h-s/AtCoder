a, b, c, d, e, f = map(int, input().split())

answer = ((a * b * c) - (d * e * f)) % 998244353

print(answer)
