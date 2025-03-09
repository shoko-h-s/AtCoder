n = int(input())
t_list = list(map(int, input().split()))
m = int(input())
px_list = [list(map(int, input().split())) for _ in range(m)]

# あらかじめ全ての合計時間を計算しておく
total_time = sum(t_list)

for px in px_list:
    t = total_time
    
    p = px[0] - 1
    x = px[1]
    
    t -= (t_list[p] - x)
    
    print(t)



# 【備考】
# Training Easy 60
