h, w = map(int, input().split())
a_list = [list(map(int, input().split())) for _ in range(h)]

# ブロックの最小値を求める
min_a = 100

for i in range(h):
    for j in range(w):
        min_a = min(min_a, a_list[i][j])

# 取り除くブロックの総数を求める
total_brock = 0

for i in range(h):
    for j in range(w):
        total_brock += a_list[i][j] - min_a

print(total_brock)
