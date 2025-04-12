n, l, r = map(int, input().split())

a_list = [i+1 for i in range(n)]

# 逆順にする部分とそうでない部分を分割 → 最後に足し合わせる
a1 = a_list[:l-1]
a2 = sorted(a_list[l-1:r], reverse=True)
a3 = a_list[r:]

b_list = a1 + a2 + a3

print(*b_list)
