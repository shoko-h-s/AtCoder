h, w = map(int, input().split())
a_list = [list(map(int, input().split())) for _ in range(h)]

for i in range(len(a_list[0])):
    tmp = []

    for a in a_list:
        tmp.append(a[i])

    print(*tmp)
