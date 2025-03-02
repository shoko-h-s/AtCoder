n, k, q = map(int, input().split())
a_list = [int(input()) for _ in range(q)]

points = [0] * n

for a in a_list:
    points[a-1] += 1
    
for p in points:
    if k - q + p > 0:
        print("Yes")
    else:
        print("No")



# 【備考】
# Training Easy 37
