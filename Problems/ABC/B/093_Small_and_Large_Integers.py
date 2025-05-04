a, b, k = map(int, input().split())

# k が a ～ b 間の整数の個数以上の場合
if k >= b - a + 1:
    new_list = [i for i in range(a, b+1)]
    
    for l in new_list:
        print(l)

else:
    s_list = [a+i for i in range(k)]
    l_list = [b-i for i in range(k)]

    new_set = set(s_list + l_list)
    new_list = list(new_set)
    new_sorted = sorted(new_list)

    for s in new_sorted:
        print(s)
