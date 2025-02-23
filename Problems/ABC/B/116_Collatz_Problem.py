s = int(input())

a_list = [s]
i = 0

while True:
    if a_list[i] % 2 == 0:
        num = a_list[i] // 2
    else:
        num = a_list[i] * 3 + 1
        
    if num in a_list:
        
        # リストに追加前にループ終了するので、インデックスは余分に 1 加算する必要あり
        print(i+2)
        break
        
    else:
        a_list.append(num)
        
    i += 1



# 【備考】
# Training Easy 20
