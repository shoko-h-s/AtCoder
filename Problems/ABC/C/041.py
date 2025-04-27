n = int(input())
a_list = list(map(int, input().split()))

# インデックスを一緒に得る
# 背の順で降順ソート
a_sorted = sorted((a, num) for num, a in enumerate(a_list, 1))
a_sorted = a_sorted[::-1]

for a in a_sorted:
    print(a[1])
