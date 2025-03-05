w = input()

# 各文字の出現回数を辞書で管理する
letters = {}

flag = True

for i in range(len(w)):
    if w[i] in letters:
        letters[w[i]] += 1
        
    else:
        letters[w[i]] = 0

for value in letters.values():
    if value % 2 != 1:
        flag = False
        print("No")
        break
        
if flag:
    print("Yes")



# 【備考】
# Training Easy 43
