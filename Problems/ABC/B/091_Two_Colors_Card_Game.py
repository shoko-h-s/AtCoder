from collections import defaultdict

n = int(input())
s_list = [input() for _ in range(n)]
m = int(input())
t_list = [input() for _ in range(m)]

st_dict = defaultdict(int)

for s in s_list:
    st_dict[s] += 1

for t in t_list:
    st_dict[t] -= 1

st_sorted = sorted(st_dict.items(), key = lambda x : x[1], reverse=True)

print(max(st_sorted[0][1], 0))
