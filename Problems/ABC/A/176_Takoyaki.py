n, x, t = map(int, input().split())

# 作る回数を求める
num = (n + x - 1) // x

print(t * num)
