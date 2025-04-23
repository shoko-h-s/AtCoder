s = input()

# 00 の部分を他の文字で書き換えてカウント
s = s.replace("00", "*")

print(len(s))
