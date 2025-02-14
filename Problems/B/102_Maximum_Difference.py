n = int(input())
a_list = list(map(int, input().split()))

# 正の整数のみ与えられるため、絶対値は考慮しなくても良い
print(max(a_list) - min(a_list))
