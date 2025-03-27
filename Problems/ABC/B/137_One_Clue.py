# 137_One_Clue

k, x = map(int, input().split())

list_1 = [i for i in range(x-k+1, x+k)]

# アンパックで出力
print(*list_1)
