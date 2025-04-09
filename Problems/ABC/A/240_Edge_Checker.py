a, b = map(int, input().split())

# 2つの数の差が1、または 9 の時（1, 10）が Yes
if (b - a == 1) or (b - a == 9):
    print("Yes")
else:
    print("No")
