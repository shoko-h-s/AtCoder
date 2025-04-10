n, k = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

flag = False

# 最大値を持つインデックスリストを作成
max_a = max(a_list)
max_a_list = [i+1 for i in range(n) if a_list[i] == max_a]

for i in range(len(max_a_list)):
    if max_a_list[i] in b_list:
        flag = True
        break
        
if flag:
    print("Yes")
else:
    print("No")
