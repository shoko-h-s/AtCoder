n, k = map(int, input().split())
h_list = list(map(int, input().split()))

count = 0

for h in h_list:
    if h >= k:
        count += 1
        
print(count)
