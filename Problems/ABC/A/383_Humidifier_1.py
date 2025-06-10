n = int(input())
tv_list = [list(map(int, input().split())) for _ in range(n)]

water = 0
before_time = 0

for i in range(n):
    down_water = tv_list[i][0] - before_time
    water = max(0, water-down_water)

    water += tv_list[i][1]

    before_time = tv_list[i][0]

print(water)
