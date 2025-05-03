import numpy as np

n = int(input())
s_list = [list(input()) for _ in range(n)]
t_list = [list(input()) for _ in range(n)]

s_array = np.array(s_list)

s_270 = np.rot90(s_array)
s_180 = np.rot90(s_array, 2)
s_90 = np.rot90(s_array, 3)

s_270 = list(s_270)
s_180 = list(s_180)
s_90 = list(s_90)

# 回転させない場合
count_0 = 0

for i in range(n):
    for j in range(n):
        if s_list[i][j] != t_list[i][j]:
            count_0 += 1

# 90度回転
count_90 = 1

for i in range(n):
    for j in range(n):
        if s_90[i][j] != t_list[i][j]:
            count_90 += 1

# 180度回転
count_180 = 2

for i in range(n):
    for j in range(n):
        if s_180[i][j] != t_list[i][j]:
            count_180 += 1

# 270度回転
count_270 = 3

for i in range(n):
    for j in range(n):
        if s_270[i][j] != t_list[i][j]:
            count_270 += 1

print(min([count_0, count_90, count_180, count_270]))
