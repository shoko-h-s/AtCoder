n = int(input())
s_list = [input() for _ in range(n)]

# 全ての単語を逆順にしたリストを作り、辞書順にソート
rev_list = [s[::-1] for s in s_list]
rev_sorted = sorted(rev_list)

# 逆順リストを元の単語に戻して順に出力
for r in rev_sorted:
    print(r[::-1])
