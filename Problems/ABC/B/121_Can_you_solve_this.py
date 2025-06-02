n, m, c = map(int, input().split())
b_list = list(map(int, input().split()))
a_list = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

for i in range(n):
    total = c

    for j in range(m):
        total += a_list[i][j] * b_list[j]

    if total > 0:
        cnt += 1

print(cnt)
