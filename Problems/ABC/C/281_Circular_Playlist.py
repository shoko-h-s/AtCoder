n, t = map(int, input().split())
a_list = list(map(int, input().split()))

# 周回部分を無視できるように操作する
sum_a = sum(a_list)
t = t % sum_a

# 各曲の開始時間リストを作成
start_list = [0] * n

for i in range(n-1):
    start_list[i+1] = start_list[i] + a_list[i]
    
for i in range(n):
    if t >= start_list[i]:
        num = i+1
        second = t - start_list[i]
        
print(num, second)
