import collections

s = list(input())

# 各文字の出現回数をリスト化する
s_count = collections.Counter(s)

# 出現回数リストの末尾を取得 → 異なる文字を特定
c = s_count.most_common()[-1][0]

answer = s.index(c) + 1

print(answer)
