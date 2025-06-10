n, m = map(int, input().split())
s_list = [input() for _ in range(n)]
t_list = [input() for _ in range(m)]

t_set = set(t_list)
cnt = 0

for s in s_list:
    if s[3:] in t_set:
        cnt += 1

print(cnt)
