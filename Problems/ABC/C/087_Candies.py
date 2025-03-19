n = int(input())
a1_list = list(map(int, input().split()))
a2_list = list(map(int, input().split()))

max_candy = 0

# どの位置で下方向に行くかで場合分けできる（n 通りある）
for i in range(n):
    a1_sum = sum(a1_list[:i+1])
    a2_sum = sum(a2_list[i:])
    
    candy = a1_sum + a2_sum
    
    if candy > max_candy:
        max_candy = candy
        
print(max_candy)



# 【備考】
# Training Easy 83
