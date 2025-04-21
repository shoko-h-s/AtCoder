s = input()

# 集合を作り、元の文字列と要素数が一致すれば yes
s_set = set(s)

if len(s) == len(s_set):
    print("yes")
else:
    print("no")



# 【備考】
# Training Easy 31
