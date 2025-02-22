n = int(input())
d_list = list(map(int, input().split()))

d_sorted = sorted(d_list)

# リストを2分割する
abc_list = d_sorted[:n//2]
arc_list = d_sorted[n//2:]

# ABCリストの最高値 < k <= ARCリストの最小値となれば良い
min_k = max(abc_list)
max_k = min(arc_list)

# ABCリストの最高値 = ARCリストの最小値の場合は、正しく分割が出来ない
if min_k == max_k:
    print(0)
else:
    print(max_k - min_k)



# 【備考】
# Training Easy 15 にも掲載
