l_list = list(map(int, input().split()))

# 正方形の場合
if l_list[0] == l_list[1] == l_list[2]:
    print(l_list[0])
    
# それ以外の場合分け    
elif l_list[0] == l_list[1]:
    print(l_list[2])
elif l_list[1] == l_list[2]:
    print(l_list[0])
else:
    print(l_list[1])
