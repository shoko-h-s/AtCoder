a = int(input())
b = int(input())

red_count = 0
blue_count = 0

# a の値を保持しておく
tmp_a = a

# 赤いボタンを押す回数を求める
while a != b:
    if a == 9:
        a = 0
    else:
        a += 1
        
    red_count += 1

# a の値を初期化
a = tmp_a

# 青いボタンを押す回数を求める
while a != b:
    if a == 0:
        a = 9
    else:
        a -= 1
        
    blue_count += 1
    
print(min(red_count, blue_count))
