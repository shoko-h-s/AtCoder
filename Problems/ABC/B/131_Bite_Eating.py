n, l = map(int, input().split())

a_list = [l + i - 1 for i in range(1, n+1)]

if 0 in a_list:
    print(sum(a_list))
else:
    min_a = 1000

    for a in a_list:
        if abs(a) < min_a:
            min_a = abs(a)
            a_num = a
    
    print(sum(a_list) - a_num)
