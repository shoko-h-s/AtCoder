n, d = map(int, input().split())
s_list = [input() for _ in range(n)]

ans = 0
days = 0

for i in range(d):
    cnt = 0

    for j in range(n):
        if s_list[j][i] == "o":
            cnt += 1
        else:
            break

    if cnt == n:
        days += 1
        ans = max(ans, days)
    else:
        days = 0

print(ans)
