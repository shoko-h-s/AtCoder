w, h = map(int, input().split())

# 比の公式
# 4 : 3 = w : h ならば、4h = 3w
if 4 * h == 3 * w:
    print("4:3")
else:
    print("16:9")
