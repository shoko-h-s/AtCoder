s = list(input())

# 偶数番目のみの桁リストを作成
s_list = [int(s[i]) for i in range(1, 17, 2)]

# 桁リストの合計が 0 ならば Yes
if sum(s_list) == 0:
    print("Yes")
else:
    print("No")
