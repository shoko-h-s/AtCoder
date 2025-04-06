s_list = [input() for _ in range(8)]

# 列名リストをあらかじめ作成
col_grid = ["a", "b", "c", "d", "e", "f", "g", "h"]

for i in range(8):
    if "*" in s_list[i]:
        line = 8 - i
        
        point = s_list[i].find("*")
        col = col_grid[point]
        
print(col + str(line))
