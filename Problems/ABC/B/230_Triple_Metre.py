s = input()

# s が 10文字以下、t は 3文字周期 → t は 12文字分用意すれば足りる
t = "oxxoxxoxxoxx"

if s in t:
    print("Yes")
else:
    print("No")
