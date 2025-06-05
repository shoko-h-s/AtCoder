n = int(input())
ab_list = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    max_d = 0
    max_j = 0

    for j in range(n):
        if i != j:
            d = ((ab_list[i][0] - ab_list[j][0])**2 + (ab_list[i][1] - ab_list[j][1])**2)**0.5
            if max_d < d:
                max_d = d
                max_j = j+1

    print(max_j)
