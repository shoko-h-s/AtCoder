h, w = map(int, input().split())
a_list = [list(map(int, input().split())) for _ in range(h)]

for i in range(h):
    line_i = ""

    for j in range(w):
        if a_list[i][j] == 0:
            line_i += "."
        else:
            c = chr(ord("A") + a_list[i][j] - 1)
            line_i += c

    print(line_i)
