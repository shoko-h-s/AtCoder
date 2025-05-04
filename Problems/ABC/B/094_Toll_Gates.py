n, m, x = map(int, input().split())
a_list = list(map(int, input().split()))

xn_count = 0
xz_count = 0

# x → n に向かう場合
for i in range(x, n+1):
    if i in a_list:
        xn_count += 1
        
# x → 0 に向かう場合（0 → x でも同様なので、そちらで実装）
for i in range(x+1):
    if i in a_list:
        xz_count += 1

# 2ルートのうち、小さい方が答え
print(min(xn_count, xz_count))
