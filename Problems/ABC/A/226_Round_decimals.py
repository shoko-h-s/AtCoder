x = input()

# 誤差対策のため、関数を使わず文字列型で実装
if int(x[-3]) < 5:
    print(int(x[:-4]))
else:
    print(int(x[:-4]) + 1)
