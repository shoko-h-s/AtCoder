n, m = map(int, input().split())
s_list = input().split()
t_list = input().split()

# 次に止まる駅とインデックスを保持する
next_i = 0
next_stop = t_list[next_i]

for s in s_list:
    if s == next_stop:
        print("Yes")
        next_i += 1
        
        if next_i < m:
            next_stop = t_list[next_i]
        
    else:
        print("No")
