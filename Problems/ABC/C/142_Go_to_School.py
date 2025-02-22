n = int(input())
a_list = list(map(int, input().split()))

# 出席番号をキーにして辞書を作成
a_keys = [i+1 for i in range(n)]
a_dic = {key:value for key, value in zip(a_keys, a_list)}

# 値でソート
a_sorted = dict(sorted(a_dic.items(), key = lambda x : x[1]))

# 辞書のキーのみを取り出す
print(" ".join(map(str, a_sorted.keys())))



# 【備考】
# Training Easy 16 にも掲載
