from collections import defaultdict

n, m = map(int, input().split())
ka_list = [list(map(int, input().split())) for _ in range(n)]

a_dict = defaultdict(int)
cnt = 0

for i in range(n):
    k = ka_list[i][0]

    for j in range(1, k+1):
        food = ka_list[i][j]
        a_dict[food] += 1

for value in a_dict.values():
    if value == n:
        cnt += 1

print(cnt)
