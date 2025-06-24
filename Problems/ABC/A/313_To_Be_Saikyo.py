n = int(input())
p_list = list(map(int, input().split()))

p_set = set(p_list)

# 人 1 が最高値で、かつ同じ数値の人がいなければ
if (max(p_list) == p_list[0]) and (p_list.count(max(p_list)) == 1):
    print(0)
else:
    print(max(p_list) - p_list[0] + 1)
