import string

# 英小文字の集合を作成
chr_list = list(string.ascii_lowercase)
chr_set = set(chr_list)

s_list = list(input())

s_set = set(s_list)

# 英小文字集合 - s に現れる文字集合の結果（差集合）をリストに直す
answer_list = list(chr_set - s_set)

answer_sorted = sorted(answer_list)

if len(answer_sorted) > 0:
    print(answer_sorted[0])
else:
    print("None")



# 【備考】
# Training Easy 35
