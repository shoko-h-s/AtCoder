n, k = map(int, input().split())
l_list = list(map(int, input().split()))

l_sorted = sorted(l_list, reverse=True)

print(sum(l_sorted[:k]))
