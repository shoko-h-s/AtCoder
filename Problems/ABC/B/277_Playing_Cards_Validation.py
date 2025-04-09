n = int(input())
s_list = [input() for _ in range(n)]

# すべての文字列は相異なるかの判定に用いる
s_set = set(s_list)

list_1 = ["H", "D", "C", "S"]
list_2 = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

flag = True

for s in s_list:
    if (s[0] not in list_1) or (s[1] not in list_2):
        flag = False
        break
        
if flag and (n == len(s_set)):
    print("Yes")
else:
    print("No")
