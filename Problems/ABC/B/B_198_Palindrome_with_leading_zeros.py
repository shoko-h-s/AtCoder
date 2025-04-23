n = input()

# 末尾の 0 を除去した文字列
n_2 = n.rstrip("0")

# 除去後の文字列が回文になっていれば、Yes
if n_2 == n_2[::-1]:
    print("Yes")
else:
    print("No")
