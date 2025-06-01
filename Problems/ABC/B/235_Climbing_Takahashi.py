n = int(input())
h_list = list(map(int, input().split()))

now_height = h_list[0]

for i in range(1, n):
    if now_height < h_list[i]:
        now_height = h_list[i]
    else:
        break

print(now_height)
