n, m, c = map(int, input().split())
b_list = list(map(int, input().split()))
a_list = [list(map(int, input().split())) for _ in range(n)]

count = 0

for a1 in a_list:
    ab_dot = 0
    
    # 各ソースコードと b_list の内積を求める
    for a, b in zip(a1, b_list):
        ab_dot += a * b
        
    if ab_dot + c > 0:
        count += 1
        
print(count)



# 【備考】
# Training Easy 5
