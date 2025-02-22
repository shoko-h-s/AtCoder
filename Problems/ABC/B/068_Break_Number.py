n = int(input())

# 負の値で初期化
max_div = -1

for i in range(1, n+1):
    count = 0
    
    # 現在のiの値を保存
    target = i

    while i % 2 == 0:
        i //= 2
        count += 1

    if count > max_div:
        max_div = count
        answer = target

print(answer)



# 【備考】
# Training Easy 11
