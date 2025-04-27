x, y = map(int, input().split())

# 両者の得点の絶対値が、3 未満であればよい
if abs(x-y) < 3:
    print("Yes")
else:
    print("No")
