# うるう年を判定する関数
def leap_year(y):
    flag = False

    if y % 400 == 0:
        flag = True
    elif y % 100 == 0:
        pass
    elif y % 4 == 0:
        flag = True

    return flag

y, m, d = map(int, input().split("/"))

success_flag = False

# 各月の最終日リスト
month_last_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 最終日リストのうるう年対応
if leap_year(y):
    month_last_day[1] = 29

# 入力年の 12/31 まで調べればよい（翌年の 1/1 は必ず割り切れる）
for i in range(m, 13):
    month_last = month_last_day[i-1]
    
    ym_mod = y % i
    
    if ym_mod == 0:
        ym = y // i
    
    if i == m:
        start_day = d
    else:
        start_day = 1
        
    for j in range(start_day, month_last+1):
        if (ym_mod == 0) and (ym % j == 0):
            success_flag = True
            
            if i <= 9:
                i = "0" + str(i)
                
            if j <= 9:
                j = "0" + str(j)
            
            print(str(y), i, j, sep="/")
            break
            
    if success_flag:
        break
        
if not success_flag:
    print(str(y+1), "01", "01", sep="/")
