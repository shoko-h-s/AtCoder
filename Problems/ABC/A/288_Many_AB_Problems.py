n = int(input())
ab_list = [list(map(int, input().split())) for i in range(n)]

for ab in ab_list:
    print(ab[0] + ab[1])
