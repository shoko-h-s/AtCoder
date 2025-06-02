n, x = map(int, input().split())
l_list = list(map(int, input().split()))

ball_location = 0
cnt = 1

for i in range(n):
    ball_location += l_list[i]

    if ball_location > x:
        break

    cnt += 1

print(cnt)
