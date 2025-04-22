s = input()
t = input()

# 次の正しい文字を保持
i = 0

list_1 = []

for j in range(len(t)):
    if t[j] == s[i]:
        list_1.append(j+1)
        i += 1
    
    # 正しい文字を入力し終わったらループを抜ける
    if i == len(s):
        break
        
print(*list_1)
