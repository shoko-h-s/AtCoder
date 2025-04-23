s = input()

s_set = set(s)

# すべて大文字、すべて小文字の両条件を否定すればよい
# 比較するためにすべて大文字、すべて小文字の両文字列を作成する
s_upper = s.upper()
s_lower = s.lower()

if (len(s) == len(s_set)) and (s != s_upper) and (s != s_lower):
    print("Yes")
else:
    print("No")
