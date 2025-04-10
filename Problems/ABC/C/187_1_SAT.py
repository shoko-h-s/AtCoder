n = int(input())

# 重複はあらかじめ省く
s_set = {input() for _ in range(n)}

# ! がついた文字列はループを回さなくてよい
# 文字列のみの場合だけをピックアップ
s0_list = [s for s in s_set if "!" not in s]

flag = True

for s in s0_list:
    if ("!" + s) in s_set:
        print(s)
        flag = False
        break
        
if flag:
    print("satisfiable")
