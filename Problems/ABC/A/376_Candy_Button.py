n, c = map(int, input().split())
t_list = list(map(int, input().split()))

cnt = 1
before_time = t_list[0]

for i in range(1, n):
    if t_list[i] - before_time >= c:
        cnt += 1
        before_time = t_list[i]

print(cnt)
