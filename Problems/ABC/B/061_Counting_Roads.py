n, m = map(int, input().split())
ab_list = [list(map(int, input().split())) for _ in range(m)]

roads = [0] * n

for ab in ab_list:
    a = ab[0] - 1
    b = ab[1] - 1
    
    roads[a] += 1
    roads[b] += 1
    
for r in roads:
    print(r)



# 【備考】
# Training Easy 53
