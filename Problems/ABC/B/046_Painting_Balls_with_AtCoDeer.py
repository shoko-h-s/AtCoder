n, k = map(int, input().split())

# 1つ目は k 通り
answer = k

# 2つ目以降は直前のボールと別の色を選択し続ければ良いので、k-1 通り
for i in range(n-1):
    answer *= (k-1)

print(answer)
