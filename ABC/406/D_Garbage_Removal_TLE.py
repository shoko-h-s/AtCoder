h, w, n = map(int, input().split())
list_xy = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
list_queries = [list(map(int, input().split())) for _ in range(q)]

for q in list_queries:
    if q[0] == 1:
        x = q[1]
        line = [xy for xy in list_xy if xy[0] == x]
        print(len(line))
        list_xy = [xy for xy in list_xy if xy not in line]

    else:
        y = q[1]
        line = [xy for xy in list_xy if xy[1] == y]
        print(len(line))
        list_xy = [xy for xy in list_xy if xy not in line]
