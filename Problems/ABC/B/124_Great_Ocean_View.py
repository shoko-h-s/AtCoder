n = int(input())
h_list = list(map(int, input().split()))

cnt = 1
max_h = h_list[0]

for i in range(1, n):
    if max_h <= h_list[i]:
        cnt += 1
        max_h = h_list[i]

print(cnt)
