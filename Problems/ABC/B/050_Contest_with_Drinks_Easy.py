n = int(input())
t_list = list(map(int, input().split()))
m = int(input())
px_list = [list(map(int, input().split())) for _ in range(m)]

total_time = sum(t_list)

for px in px_list:
    p = px[0] - 1
    x = px[1]
    ans_time = total_time - t_list[p] + x
    print(ans_time)
