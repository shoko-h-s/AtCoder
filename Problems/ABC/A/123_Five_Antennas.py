abcde_list = [int(input()) for _ in range(5)]
k = int(input())

# 最も距離が離れている組で判定
if abcde_list[4] - abcde_list[0] > k:
    print(":(")
else:
    print("Yay!")
