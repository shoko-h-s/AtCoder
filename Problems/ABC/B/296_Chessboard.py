s_list = [input() for _ in range(8)]

for i in range(8):
    if s_list[i].count("*") == 1:

        for j in range(8):
            if s_list[i][j] == "*":
                print(chr(ord("a") + j) + str(8-i))
                break

