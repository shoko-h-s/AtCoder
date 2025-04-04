import collections

n = int(input())
s_list = [input() for _ in range(n)]
m = int(input())
t_list = [input() for _ in range(m)]

# s_list への出現回数を元に、点数リストを作る
point_list = collections.Counter(s_list)

# t_list の出現回数を、point_list に反映する
for t in t_list:
    if t in point_list:
        point_list[t] -= 1
    else:
        point_list[t] = -1
        
# point_list の最大値を取得
max_point = max(point_list.values())

# ポイントの最大値と 0 、大きい方が答え
print(max(max_point, 0))
