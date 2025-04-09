s, t, x = map(int, input().split())

# 日付が変わっている場合の処理
if s > t:
    if (s <= x) or (x < t):
        print("Yes")
    else:
        print("No")
        
else:
    if (s <= x < t):
        print("Yes")
    else:
        print("No")
