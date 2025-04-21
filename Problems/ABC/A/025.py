s = input()
n = int(input())

name_list = []

# 全呼び名のリストを作る
for i in range(5):
    for j in range(5):
        name = s[i] + s[j]
        name_list.append(name)
        
print(name_list[n-1])
