s = input()

# 考えうる2パターンを準備しておく
list_1 = ["0" if i % 2 == 0 else "1" for i in range(len(s))]
pattern_1 = "".join(list_1)
list_2 = ["1" if i % 2 == 0 else "0" for i in range(len(s))]
pattern_2 = "".join(list_2)

tile_1 = 0
tile_2 = 0

# どちらかのパターンと一致していれば塗り替え不要
if (s == pattern_1) or (s == pattern_2):
    print(0)

# 2パターンと一致している個数を調べる
# どちらか片方だけ調べれば良い
else:
    for i in range(len(s)):
        if s[i] == pattern_1[i]:
            tile_1 += 1
        else:
            tile_2 += 1
            
    if tile_1 < tile_2:
        print(tile_1)
    else:
        print(tile_2)
  


# 【備考】
# Training Easy 44
