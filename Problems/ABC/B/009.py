n = int(input())
a_list = [int(input()) for _ in range(n)]

# 重複要素を取り除いてから、再度リスト形式に戻す
a_set = set(a_list)
a_list = list(a_set)

a_sorted = sorted(a_list, reverse=True)

print(a_sorted[1])
