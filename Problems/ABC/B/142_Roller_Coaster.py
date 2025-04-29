n, k = map(int, input().split())
h_list = list(map(int, input().split()))

hk_list = [h for h in h_list if h >= k]

print(len(hk_list))
