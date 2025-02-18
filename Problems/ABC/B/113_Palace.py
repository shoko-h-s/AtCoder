n = int(input())
t, a = map(int, input().split())
h_list = list(map(int, input().split()))

d_list = [t - h * 0.006 for h in h_list]
ah_list = [abs(a - d) for d in d_list]

print(ah_list.index(min(ah_list)) + 1)
