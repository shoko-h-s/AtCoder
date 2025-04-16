import math

n, m = map(int, input().split())

# 2つの和が偶数になる → 2つの値の偶奇が一致している
# n から2つ選ぶ、m から2つ選ぶの合計が答え
comb_n = math.comb(n, 2)
comb_m = math.comb(m, 2)

print(comb_n + comb_m)
