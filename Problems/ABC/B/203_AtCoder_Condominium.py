n, k = map(int, input().split())

total = 0

for i in range(1, n+1):
    for j in range(1, k+1):
        room_num = i * 100 + j
        total += room_num

print(total)
