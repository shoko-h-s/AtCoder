h, w = map(int, input().split())
s_list = [input() for _ in range(h)]

for i in range(h):
    line = ""

    for j in range(w):
        if s_list[i][j] == "#":
            line += "#"

        else:
            cnt = 0

            # 上
            if i > 0:
                if s_list[i-1][j] == "#":
                    cnt += 1

                # 左上
                if j > 0:
                    if s_list[i-1][j-1] == "#":
                        cnt += 1

                # 右上
                if j < w-1:
                    if s_list[i-1][j+1] == "#":
                        cnt += 1

            # 下
            if i < h-1:
                if s_list[i+1][j] == "#":
                    cnt += 1

                # 左下
                if j > 0:
                    if s_list[i+1][j-1] == "#":
                        cnt += 1

                # 右下
                if j < w-1:
                    if s_list[i+1][j+1] == "#":
                        cnt += 1

            # 左
            if j > 0:
                if s_list[i][j-1] == "#":
                    cnt += 1

            # 右
            if j < w-1:
                if s_list[i][j+1] == "#":
                    cnt += 1

            line += str(cnt)

    print(line)
