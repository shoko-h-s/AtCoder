from collections import defaultdict

n, m = map(int, input().split())
ab_list = [list(map(int, input().split())) for _ in range(m)]

d = defaultdict(int)

for ab in ab_list:
    d[ab[0]] += 1
    d[ab[1]] += 1

count = sum(v == 2 for v in d.values())

if n == count == len(d):
    print("Yes")
else:
    print("No")
