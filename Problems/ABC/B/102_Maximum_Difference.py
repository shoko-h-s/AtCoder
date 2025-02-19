n = int(input())
a_list = list(map(int, input().split()))

# 正の整数のみ与えられるため、絶対値は考慮しなくても良い
print(max(a_list) - min(a_list))



# 【別解】全探索で解く場合

# n = int(input())
# a_list = list(map(int, input().split()))

# # 先頭の値で初期化
# max_a = a_list[0]
# min_a = a_list[0]

# for i in range(1, n):
#     if a_list[i] > max_a:
#         max_a = a_list[i]
        
#     if a_list[i] < min_a:
#         min_a = a_list[i]
        
# print(max_a - min_a)
