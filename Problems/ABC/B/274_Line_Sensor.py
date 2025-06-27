h, w = map(int, input().split())
grids = [input() for _ in range(h)]

ans_list = []

for i in range(w):
    box = 0

    for j in range(h):
        if grids[j][i] == "#":
            box += 1

    ans_list.append(box)

print(*ans_list)
