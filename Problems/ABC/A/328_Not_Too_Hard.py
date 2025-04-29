n, x = map(int, input().split())
s_list = list(map(int, input().split()))

# 内包表記で else を使わない場合、if は末尾に持ってくる
sx_list = [s for s in s_list if s <= x]

print(sum(sx_list))
