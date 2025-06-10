n, m, t = map(int, input().split())
ab_list = [list(map(int, input().split())) for _ in range(m)]

flag = True
battery = n
before_time = 0

for ab in ab_list:
    battery -= ab[0] - before_time

    if battery <= 0:
        flag = False
        break

    charge = ab[1] - ab[0]
    battery = min(n, battery + charge)
    before_time = ab[1]

# 最後のカフェ～帰宅時の処理
battery -= t - before_time

if flag and (battery > 0):
    print("Yes")
else:
    print("No")
