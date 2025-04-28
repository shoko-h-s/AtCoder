x = input()

# 誤差を防ぐため、小数は文字列を経由して処理
if "." in x:
    x = x.split(".")
    print(x[0])
else:
    print(int(x))
