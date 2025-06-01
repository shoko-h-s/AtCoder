N, T = map(int, input().split())

route_list = []

for _ in range(N):
    c, t = map(int, input().split())

    if t <= T:
        route_list.append(c)

if len(route_list) > 0:
    print(min(route_list))
else:
    print("TLE")
