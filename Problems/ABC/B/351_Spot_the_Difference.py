n = int(input())
a_list = [input() for _ in range(n)]
b_list = [input() for _ in range(n)]

for i in range(n):
    if a_list[i] != b_list[i]:

        for j in range(n):
            if a_list[i][j] != b_list[i][j]:
                print(i+1, j+1)
                break
