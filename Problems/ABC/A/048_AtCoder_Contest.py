# スペース区切りのリスト形式で入力を受け取る
str = input().split()

# 必要なのは 2番目の要素のみ
s = str[1]

# 2番目の要素の最初の文字を抽出、文字列を結合
# s[0] は、 str[1][0] としても良い
print("A" + s[0] + "C")



# 提出コード
# https://atcoder.jp/contests/abc048/submissions/64129333
