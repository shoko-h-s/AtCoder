n, k = map(int, input().split())
p_list = list(map(int, input().split()))

p_sorted = sorted(p_list)

print(sum(p_sorted[:k]))
