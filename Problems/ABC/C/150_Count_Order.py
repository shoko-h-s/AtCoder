import itertools

n = int(input())
p_tuple = tuple(map(int, input().split()))
q_tuple = tuple(map(int, input().split()))

# 順列を全て列挙したリストを作り、辞書順にソートする
per_list = list(itertools.permutations(p_tuple))
per_sorted = sorted(per_list)

a = per_sorted.index(p_tuple) + 1
b = per_sorted.index(q_tuple) + 1

print(abs(a - b))



# 【備考】
# Training Easy 25
