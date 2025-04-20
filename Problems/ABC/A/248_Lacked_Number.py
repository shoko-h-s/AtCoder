s = list(input())

# リストで受け取った文字列を、昇順にソート
s_sorted = sorted(s)

flag = False

# 昇順に並べた文字列と、インデックスを比較
# 一致しないインデックスが答え
for i in range(9):
    if int(s_sorted[i]) != i:
        print(i)
        flag = True
        break
        
# 昇順に並べた文字列と一致し続けた場合は、9 が答え
if not flag:
    print(9)
