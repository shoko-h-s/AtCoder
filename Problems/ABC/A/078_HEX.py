x, y = input().split()

# 10進数に変換
x_10 = int(x, 16)
y_10 = int(y, 16)

if x < y:
    print("<")
elif x > y:
    print(">")
else:
    print("=")
