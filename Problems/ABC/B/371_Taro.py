n, m = map(int, input().split())
ab_list = [list(input().split()) for _ in range(m)]

# 太郎がいるかどうかのチェックリスト
taro_list = [0 for _ in range(n)]

for ab in ab_list:
    i = int(ab[0]) - 1
    
    if (ab[1] == "M") and (taro_list[i] == 0):
        print("Yes")
        taro_list[i] = 1 
        
    else:
        print("No")
