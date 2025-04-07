s = input()

# 末尾 3 文字を整数型に直す
num = int(s[3:])

if (1 <= num <= 349) and (num != 316):
    print("Yes")
else:
    print("No")
