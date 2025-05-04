n = int(input())
xy_list = [list(map(int, input().split())) for _ in range(n)]

max_length = 0

for i in range(n):
    for j in range(n):
        if i <= j:

            # 平方根は最後に取る
            length = (xy_list[j][0] - xy_list[i][0])**2 + (xy_list[j][1] - xy_list[i][1])**2

            max_length = max(max_length, length)

print(max_length**0.5)
