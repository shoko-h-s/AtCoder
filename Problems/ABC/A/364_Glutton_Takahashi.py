n = int(input())
s_list = [input() for _ in range(n)]

flag = True

for i in range(1, n):
    if (s_list[i-1] == "sweet") and (s_list[i] == "sweet"):
        
        # i が最後である場合は Yes 判定
        if i != n-1:
            flag = False
        
if flag:
    print("Yes")
else:
    print("No")
