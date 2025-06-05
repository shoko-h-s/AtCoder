n = int(input())
ab_list = [list(map(int, input().split())) for _ in range(n)]

ab_time = (10**5) * 2
a_b_time = (10**5) * 2

for ab in ab_list:
    ab_time = min(ab_time, ab[0] + ab[1])

for i in range(n):
    for j in range(n):
        if i != j:
            ij_time = max(ab_list[i][0], ab_list[j][1])
            a_b_time = min(a_b_time, ij_time)

print(min(ab_time, a_b_time))
