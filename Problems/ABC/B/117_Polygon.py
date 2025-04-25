n = int(input())
l_list = list(map(int, input().split()))

# 他の n−1 辺の長さの合計
total_side = sum(l_list) - max(l_list)

if max(l_list) < total_side:
    print("Yes")
else:
    print("No")
