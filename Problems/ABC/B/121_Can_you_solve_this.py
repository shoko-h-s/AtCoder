n, m, c = map(int, input().split())
b_list = list(map(int, input().split()))
a_list = [list(map(int, input().split())) for _ in range(n)]

count = 0

for i in range(n):
    total = 0
    
    for j in range(m):
        total += a_list[i][j] * b_list[j]
        
    if total + c > 0:
        count += 1
        
print(count)



# 【備考】
# Training Easy 5 にも掲載
