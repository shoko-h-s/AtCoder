n, m = map(int, input().split())
s_list = [input() for _ in range(n)]

cnt = 0

for i in range(n):
    for j in range(i+1, n):
        flag = True

        for k in range(m):
            if s_list[i][k] == s_list[j][k] == "x":
                flag = False
                break

        if flag:
            cnt += 1

print(cnt)Let's Get a Perfect Score
