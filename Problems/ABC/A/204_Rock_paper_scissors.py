x, y = map(int, input().split())

if x == y:
    print(x)
    
else:
    # x, y をリスト化する
    list_1 = [x, y]
    
    # 0-2 のうち、リストに含まれていないものが答え
    if list_1.count(0) == 0:
        print(0)
    elif list_1.count(1) == 0:
        print(1)
    else:
        print(2)
