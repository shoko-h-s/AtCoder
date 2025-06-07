s = input()
t = input()

flag = False

if s == t:
    flag = True
else:
    for i in range(len(s)-1):
        # 操作用のコピーをリストで準備
        s_copy_list = list(s)

        s_copy_list[i], s_copy_list[i+1] = s_copy_list[i+1], s_copy_list[i]
        s_copy = ("".join(s_copy_list))

        if s_copy == t:
            flag = True
            break

if flag:
    print("Yes")
else:
    print("No")
