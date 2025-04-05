n, t, a = map(int, input().split())

# 残りの票数を求める
rest_vort = n - t - a

# 票が多い方、少ない方をそれぞれ求める
g_vort = max(t, a)
l_vort = min(t, a)

# 票が少ない方に全ての残り票が入った場合で場合分け
if g_vort > l_vort + rest_vort:
    print("Yes")
else:
    print("No")
