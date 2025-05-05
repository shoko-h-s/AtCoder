from collections import defaultdict

n, m = map(int, input().split())
ab_list = [list(map(int, input().split())) for _ in range(n)]

ab_dic = defaultdict(int)

for ab in ab_list:
    ab_dic[ab[0]] += ab[1]

ab_sorted = sorted(ab_dic.items())

drink = m
i = 0
price = 0

while drink > 0:
    price += ab_sorted[i][0] * min(drink, ab_sorted[i][1])
    drink -= ab_sorted[i][1]
    i += 1

print(price)
