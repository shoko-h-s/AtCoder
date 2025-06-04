s_list = list(map(int, input().split()))

flag = True

# 広義単調増加のチェック
for i in range(7):
    if s_list[i] > s_list[i+1]:
        flag = False
        break

# その他のチェック
if flag:
    for s in s_list:
        if (s < 100) or (s > 675) or (s % 25 != 0):
            flag = False
            break

if flag:
    print("Yes")
else:
    print("No")
