n = int(input())
s = input().split("|")

# | で分割した2番目のブロックで判定する
if "*" in s[1]:
    print("in")
else:
    print("out")
