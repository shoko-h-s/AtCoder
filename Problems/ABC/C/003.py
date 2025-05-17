n, k = map(int, input().split())
list_r = list(map(int, input().split()))

# リストを降順ソート → リストから K 個抽出 → 昇順にソート
list_r.sort(reverse=True)
list_rk = list_r[:k]
list_rk.sort()

rate = 0

for rk in list_rk:
    rate = (rate + rk) / 2

print(rate)
