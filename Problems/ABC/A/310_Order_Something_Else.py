n, p, q = map(int, input().split())
d_list = list(map(int, input().split()))

print(min(p, q + min(d_list)))
